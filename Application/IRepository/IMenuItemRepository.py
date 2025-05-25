from abc import ABC, abstractmethod
from typing import List, Optional

from Domain import models
from Application import schemas


class IMenuItemRepository(ABC):
    @abstractmethod
    def create_menu_item(self, item: schemas.CreateMenuItemDto) -> models.MenuItem:
        pass

    @abstractmethod
    def get_menu_item(self, menu_item_id: int) -> Optional[models.MenuItem]:
        pass

    @abstractmethod
    def get_menu_items(self) -> List[models.MenuItem]:
        pass

    @abstractmethod
    def update_menu_item(self, menu_item_id: int, menu_item: schemas.CreateMenuDto) -> models.MenuItem:
        pass

    @abstractmethod
    def delete_menu_item(self, menu_item_id: int) -> dict:
        pass

