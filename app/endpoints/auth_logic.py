from typing import Iterable

from fastapi import Depends, HTTPException
from starlette import status

from Application import schemas
from Infrastracture.DependencyInjection import get_user_repository
from Infrastracture.Repository import UserRepository
from app.dependency import oauth2_scheme


def get_current_user(
    token: str = Depends(oauth2_scheme),
    repo : UserRepository = Depends(get_user_repository)
) -> schemas.UserResponse:
    user = repo.get_current_user(token)
    if user is None:
        raise HTTPException(status_code=401, detail='Invalid or expired credentials')
    return user

def require_roles(*allowed_roles: Iterable[str]):
    def _role_checker(
        current: schemas.UserResponse = Depends(get_current_user),
    ) -> schemas.UserResponse:
        if current.role.role_name not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )
        return current

    return _role_checker