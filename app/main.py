from datetime import timedelta

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import  OAuth2PasswordRequestForm
from starlette import status

from Application.Config import ACCESS_TOKEN_EXPIRE_MINUTES
from Application.schemas import Token
from Infrastracture.Repository import UserRepository
from Application import schemas
from Infrastracture.DependencyInjection import get_user_repository
from app.dependency import oauth2_scheme
from app.endpoints import menus, menu_items, users, roles

app = FastAPI()

def get_current_user(
        token: str = Depends(oauth2_scheme), repo: UserRepository = Depends(get_user_repository)) -> schemas.UserResponse:
    return repo.get_current_user(token)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    raise HTTPException(status_code=302, headers={"Location": "/docs"})

app.include_router(menus.router)
app.include_router(menu_items.router)
app.include_router(users.router)
app.include_router(roles.router)

@app.post("/token", response_model=Token, summary="JWT", include_in_schema=False)
def login(form_data: OAuth2PasswordRequestForm = Depends(), repo: UserRepository = Depends(get_user_repository)):
    user = repo.get_user_by_username(form_data.username)
    if not user or not repo.verify_password(form_data.password, user.hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")
    access_token = repo.create_access_token({"sub": user.username},timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}
