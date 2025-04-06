from abc import ABC, abstractmethod
from typing import List, Optional

from Domain import models
from Infrastracture import schemas


class IMenuRepository(ABC):
    @abstractmethod
    def create_menu(self, item: schemas.CreateMenuDto) -> models.Menu:
        pass

    @abstractmethod
    def get_menu(self, menu_id: int) -> Optional[models.Menu]:
        pass

    @abstractmethod
    def get_menus(self) -> List[models.Menu]:
        pass

    @abstractmethod
    def update_menu(self, menu_id: int, menu_update: schemas.CreateMenuDto) -> models.Menu:
        pass

    @abstractmethod
    def delete_menu(self, menu_id: int) -> dict:
        pass
