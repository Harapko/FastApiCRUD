from fastapi import APIRouter, Depends

from Application import schemas
from Infrastracture.DependencyInjection import get_role_repository
from Infrastracture.Repository import RoleRepository
from app.endpoints.auth_logic import require_roles

router = APIRouter(prefix="/roles", tags=["Roles"], dependencies=[Depends(require_roles("Admin"))])

@router.post("", response_model=schemas.RoleResponse)
def create_role(role: schemas.CreateRoleDto, repo: RoleRepository = Depends(get_role_repository)):
    return repo.create_role(role)

@router.get("", response_model=list[schemas.RoleResponse])
def get_roles(repo: RoleRepository = Depends(get_role_repository)):
    return repo.get_roles()

@router.get("/{id}", response_model=schemas.RoleResponse)
def get_role(id: int, repo: RoleRepository = Depends(get_role_repository)):
    role = repo.get_role(id)
    return role

@router.put("/{id}", response_model=schemas.RoleResponse)
def update_role(id: int, role: schemas.CreateRoleDto, repo: RoleRepository = Depends(get_role_repository)):
    return repo.update_role(id, role)

@router.delete("/{id}")
def delete_role(id: int, repo: RoleRepository = Depends(get_role_repository)):
    return repo.delete_role(id)