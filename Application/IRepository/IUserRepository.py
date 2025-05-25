from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Optional, List

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from Application import schemas
from Domain import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user: schemas.CreateUserDto) -> models.User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[models.User]:
        pass

    @abstractmethod
    def get_users(self) -> List[models.User]:
        pass

    @abstractmethod
    def update_user(self, user_id : int, user: schemas.CreateUserDto) -> models.User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def verify_password(self, plain: str, hashed: str) -> bool:
        pass

    @abstractmethod
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        pass

    @abstractmethod
    def get_current_user(self, token: str = Depends(oauth2_scheme)) -> models.User:
        pass