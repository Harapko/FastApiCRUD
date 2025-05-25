from fastapi import APIRouter, Depends

from Application import schemas
from Infrastracture.DependencyInjection import get_menu_item_repository
from Infrastracture.Repository import MenuItemRepository

router = APIRouter(prefix="/menu_item", tags=["MenuItems"], )

@router.post("", response_model=schemas.MenuItemResposne)
def create_item(menu_item: schemas.CreateMenuItemDto, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    return  repo.create_menu_item(menu_item)

@router.get("s", response_model=list[schemas.MenuItemResposne])
def get_menu_items(repo: MenuItemRepository = Depends(get_menu_item_repository)):
    menu_items = repo.get_menu_items()
    return menu_items

@router.get("{id}", response_model=schemas.MenuItemResposne)
def get_menu_item(id: int, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    menu_item = repo.get_menu_item(id)
    return menu_item

@router.get("/{menu_id}", response_model=list[schemas.MenuItemResposne])
def read_items(menu_id: int, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    menu_items = repo.get_menu_items_by_menu_id(menu_id)
    return menu_items

@router.put("/{id}", response_model=schemas.MenuItemResposne)
def update_menu_item(
        id: int, menu_item: schemas.CreateMenuItemDto, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    return repo.update_menu_item(id, menu_item)

@router.delete("/{id}")
def delete_menu_item(id: int, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    repo.delete_menu_item(id)