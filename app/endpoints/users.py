from fastapi import APIRouter, Depends

from Application import schemas
from Infrastracture.DependencyInjection import get_user_repository
from Infrastracture.Repository import UserRepository
from app.endpoints.auth_logic import require_roles

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=schemas.UserResponse)
def create_user(user: schemas.CreateUserDto, repo: UserRepository = Depends(get_user_repository)):
    return repo.create_user(user)

@router.get("", response_model=list[schemas.UserResponse])
def get_users(repo: UserRepository = Depends(get_user_repository)):
    return repo.get_users()

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, repo: UserRepository = Depends(get_user_repository), ):
    user = repo.get_user(id)
    return user

@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(id: int, user: schemas.CreateUserDto, repo: UserRepository = Depends(get_user_repository)):
    return repo.update_user(id, user)

@router.delete("/{id}", )
def delete_user(id: int, repo: UserRepository = Depends(get_user_repository)):
    return repo.delete_user(id)
