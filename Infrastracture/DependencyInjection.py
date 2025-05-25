from fastapi import Depends
from sqlalchemy.orm import Session

from .Repository import MenuRepository, MenuItemRepository, UserRepository, RoleRepository
from Infrastracture.Repository.MenuRepository import DBMenuRepository
from Infrastracture.Repository.MenuItemRepository import DBMenuItemRepository
from .Repository.RoleRepository import DBRoleRepository
from .Repository.UserRepository import DBUserRepository
from .database import get_db


def get_menu_item_repository(db: Session = Depends(get_db)) -> MenuItemRepository:
    return DBMenuItemRepository(db)

def get_menu_repository(db: Session = Depends(get_db)) -> MenuRepository:
    return DBMenuRepository(db)

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return DBUserRepository(db)

def get_role_repository(db: Session = Depends(get_db)) -> RoleRepository:
    return DBRoleRepository(db)