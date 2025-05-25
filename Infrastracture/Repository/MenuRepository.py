from typing import Optional, List

from sqlalchemy.orm import Session
from fastapi import HTTPException

from Application.IRepository.IMenuRepository import IMenuRepository
from Domain import models
from Application import schemas


class DBMenuRepository(IMenuRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_menu(self, menu: schemas.CreateMenuDto) -> models.Menu:
        db_menu = models.Menu(**menu.dict())
        self.db.add(db_menu)
        self.db.commit()
        self.db.refresh(db_menu)
        return db_menu

    def get_menu(self, menu_id: int) -> Optional[models.Menu]:
        menu = self.db.query(models.Menu).filter(models.Menu.id == menu_id).first()
        if not menu:
            raise HTTPException(status_code=404, detail="Menu not found")
        return menu

    def get_menus(self) -> List[models.Menu]:
        return self.db.query(models.Menu).all()

    def update_menu(self, menu_id: int, menu_update: schemas.CreateMenuDto) -> models.Menu:
        menu = self.get_menu(menu_id)
        if not menu:
            raise HTTPException(status_code=404, detail="Menu not found")
        for key, value in menu_update.dict().items():
            setattr(menu, key, value)
        self.db.commit()
        self.db.refresh(menu)
        return menu

    def delete_menu(self, menu_id: int) -> dict:
        menu = self.get_menu(menu_id)
        if not menu:
            raise HTTPException(status_code=404, detail="Menu not found")
        self.db.delete(menu)
        self.db.commit()
        return {"detail": "Menu deleted"}
