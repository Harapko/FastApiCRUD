from datetime import timedelta, datetime
from typing import Optional, List

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from Application import schemas
from Application.Config import SECRET_KEY, ALGORITHM
from Application.IRepository.IUserRepository import IUserRepository
from Domain import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class DBUserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.CreateUserDto) -> models.User:
        db_user = models.User()
        db_user.username = user.username
        db_user.role_id = user.role_id
        db_user.hash = pwd_context.hash(user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int) -> Optional[models.User]:
        user = self.db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_user_by_username(self, username: str) -> Optional[models.User]:
        user = self.db.query(models.User).filter(models.User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_users(self) -> List[models.User]:
        return self.db.query(models.User).all()

    def update_user(self, user_id: int, user_update: schemas.CreateUserDto) -> models.User:
        user = self.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        for key, value in user_update.dict().items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, id: int) -> dict:
        user = self.get_user(id)
        self.db.delete(user)
        self.db.commit()
        return {"detail": f"User with id '{id}' deleted"}

    def verify_password(self, plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def get_current_user(self, token: str = Depends(oauth2_scheme)) -> models.User:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise "Could not validate credentials"
        except JWTError:
            raise "Could not validate credentials"

        user_record = self.get_user_by_username(username)
        if user_record is None:
            raise "Could not validate credentials"
        return user_record
