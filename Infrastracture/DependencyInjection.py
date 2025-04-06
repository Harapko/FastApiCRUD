from fastapi import Depends
from sqlalchemy.orm import Session

from . import MenuItemRepository, MenuRepository
from .MenuRepository import DBMenuRepository
from .MenuItemRepository import DBMenuItemRepository
from .database import get_db


def get_menu_item_repository(db: Session = Depends(get_db)) -> MenuItemRepository:
    return DBMenuItemRepository(db)

def get_menu_repository(db: Session = Depends(get_db)) -> MenuRepository:
    return DBMenuRepository(db)
