from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from Application import schemas
from Application.IRepository.IRoleRepository import IRoleRepository
from Domain import models


class DBRoleRepository(IRoleRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_role(self, role: schemas.CreateRoleDto) -> models.Role:
        db_role = models.Role(**role.dict())
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role

    def get_roles(self) -> List[models.Role]:
        return self.db.query(models.Role).all()

    def get_role(self, id: int) -> models.Role:
        role = self.db.query(models.Role).filter(models.Role.id == id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    def update_role(self, id: int, role_updated: schemas.CreateRoleDto) -> models.Role:
        role = self.get_role(id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        for key, value in role_updated.dict().items():
            setattr(role, key, value)
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete_role(self, id: int):
        role = self.get_role(id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        self.db.delete(role)
        self.db.commit()
        return {"detail": "Role deleted"}