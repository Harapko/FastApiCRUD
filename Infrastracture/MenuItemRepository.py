from typing import Optional, List

from sqlalchemy.orm import Session
from fastapi import HTTPException

from Application.IMenuItemRepository import IMenuItemRepository
from Domain import models
from Infrastracture import schemas


class DBMenuItemRepository(IMenuItemRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_menu_item(self, menu_item: schemas.CreateMenuItemDto) -> models.MenuItem:
        db_menu_item = models.MenuItem(**menu_item.dict())
        db_menu = self.db.query(models.Menu).filter(models.Menu.id == db_menu_item.menu_id).first()

        if not db_menu:
            raise HTTPException(status_code=404, detail=f"Menu with id {db_menu_item.menu_id} not found")

        self.db.add(db_menu_item)
        self.db.commit()
        self.db.refresh(db_menu_item)
        return db_menu_item

    def get_menu_item(self, menu_item_id: int) -> Optional[models.MenuItem]:
        menu_item = self.db.query(models.MenuItem).filter(models.MenuItem.id == menu_item_id).first()
        return menu_item

    def get_menu_items_by_menu_id(self, menu_id: int) -> List[models.MenuItem]:
        menu_items = self.db.query(models.MenuItem).filter(models.MenuItem.menu_id == menu_id).all()
        return menu_items

    def get_menu_items(self) -> List[models.MenuItem]:
        return self.db.query(models.MenuItem).all()

    def update_menu_item(self, menu_item_id: int, menu_item_update: schemas.CreateMenuItemDto) -> models.MenuItem:
        menu_item = self.get_menu_item(menu_item_id)
        if not menu_item:
            raise HTTPException(status_code=404, detail="Menu item not found")
        for key, value in menu_item_update.dict().items():
            setattr(menu_item, key, value)
        self.db.commit()
        self.db.refresh(menu_item)
        return menu_item

    def delete_menu_item(self, menu_item_id: int) -> dict:
        menu_item = self.get_menu_item(menu_item_id)
        if not menu_item:
            raise HTTPException(status_code=404, detail="Menu item not found")
        self.db.delete(menu_item)
        self.db.commit()
        return {"detail": "Menu item deleted"}
