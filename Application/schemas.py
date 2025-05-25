from typing import List

from pydantic import BaseModel, validator


class CreateMenuItemDto(BaseModel):
    menu_item_name: str
    display_order: int
    menu_id: int

    @validator("menu_item_name")
    def validate_menu_item_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("menu_item_name field cannot be empty")
        return value

    @validator("display_order")
    def validate_display_order(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("display_order cannot be less than 0")
        return value

class MenuItemResposne(BaseModel):
    id: int
    menu_item_name: str
    display_order: int

class CreateMenuDto(BaseModel):
    menu_name: str

    @validator("menu_name")
    def validate_menu_item_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("menu_name field cannot be empty")
        return value

class MenuResposne(BaseModel):
    id: int
    menu_name: str
    menu_items: List[MenuItemResposne]

class CreateUserDto(BaseModel):
    username: str
    password: str
    role_id: int

class UserResponse(BaseModel):
    id: int
    username: str
    role_id: int

class CreateRoleDto(BaseModel):
    role_name: str

class RoleResponse(BaseModel):
    id: int
    role_name: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    username: str
    password: str

    class Config:
        model_config = {"from_attributes": True}
