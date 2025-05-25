from abc import ABC, abstractmethod
from typing import List, Optional

from Application import schemas
from Domain import models


class IRoleRepository(ABC):
    @abstractmethod
    def create_role(self, role: schemas.CreateRoleDto) -> models.Role:
        pass

    @abstractmethod
    def get_roles(self) -> List[models.Role]:
        pass

    @abstractmethod
    def get_role(self, role_id: int) -> Optional[models.Role]:
        pass

    @abstractmethod
    def update_role(self, role_id: int, role: schemas.CreateRoleDto) -> models.Role:
        pass

    @abstractmethod
    def delete_role(self, role_id: int) -> dict:
        pass