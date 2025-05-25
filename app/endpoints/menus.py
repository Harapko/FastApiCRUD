from http.client import HTTPException

from Application import schemas
from Infrastracture.DependencyInjection import get_menu_repository
from Infrastracture.Repository import MenuRepository

from fastapi import APIRouter, Depends, HTTPException

from app.endpoints.auth_logic import require_roles

router = APIRouter(prefix="/menus", tags=["Menus"])

@router.post("", response_model=schemas.MenuResposne, dependencies=[Depends(require_roles("Admin"))])
def create_menu(menu: schemas.CreateMenuDto,repo: MenuRepository = Depends(get_menu_repository)):
    return  repo.create_menu(menu)

@router.get(
    "", response_model=list[schemas.MenuResposne], dependencies=[Depends(require_roles("Admin", "Waiter"))])
def read_items(repo: MenuRepository = Depends(get_menu_repository)):
    menus = repo.get_menus()
    return menus

@router.get("/{id}", response_model=schemas.MenuResposne, dependencies=[Depends(require_roles("Admin", "Waiter"))])
def read_menu(id: int, repo: MenuRepository = Depends(get_menu_repository)):
    menu = repo.get_menu(id)
    if menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu

@router.put("/{id}", response_model=schemas.MenuResposne, dependencies=[Depends(require_roles("Admin"))])
def update_menu(id: int, menu_update: schemas.CreateMenuDto, repo: MenuRepository = Depends(get_menu_repository)):
    item = repo.update_menu(id, menu_update)
    return item

@router.delete("/{id}", dependencies=[Depends(require_roles("Admin"))])
def delete_menu(id: int, repo: MenuRepository = Depends(get_menu_repository)):
    repo.delete_menu(id)
    return True
