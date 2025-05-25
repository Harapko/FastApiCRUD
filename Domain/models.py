from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Infrastracture.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    menu_item_name = Column(String, index=True)
    display_order = Column(Integer, index=True)
    menu_id = Column(Integer, ForeignKey("menus.id"), index=True)
    menu = relationship("Menu", back_populates="menu_items")

class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    menu_name = Column(String, index=True)
    menu_items = relationship("MenuItem", back_populates="menu")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hash = Column(String, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"), index=True)
    role = relationship("Role", back_populates="users")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, index=True)
    users = relationship("User", back_populates="role")