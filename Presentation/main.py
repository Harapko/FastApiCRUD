from fastapi import FastAPI, HTTPException, Depends
from Infrastracture import schemas, MenuItemRepository, MenuRepository
from Domain import models
from Infrastracture.DependencyInjection import get_menu_item_repository, get_menu_repository
from Infrastracture.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    raise HTTPException(status_code=302, headers={"Location": "/docs"})

@app.post("/menu/", response_model=schemas.MenuResposne, tags=["Menus"])
def create_menu(menu: schemas.CreateMenuDto, repo: MenuRepository = Depends(get_menu_repository)):
    return  repo.create_menu(menu)

@app.get("/menus/", response_model=list[schemas.MenuResposne], tags=["Menus"])
def read_items(repo: MenuRepository = Depends(get_menu_repository)):
    menus = repo.get_menus()
    return menus

@app.get("/menu/{item_id}", response_model=schemas.MenuResposne, tags=["Menus"])
def read_menu(menu_id: int, repo: MenuRepository = Depends(get_menu_repository)):
    menu = repo.get_menu(menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu

@app.put("/menu/{item_id}", response_model=schemas.MenuResposne, tags=["Menus"])
def update_menu(menu_id: int, menu_update: schemas.CreateMenuDto, repo: MenuRepository = Depends(get_menu_repository)):
    item = repo.update_menu(menu_id, menu_update)
    return item

@app.delete("/menu/{item_id}", tags=["Menus"])
def delete_menu(menu_id: int, repo: MenuRepository = Depends(get_menu_repository)):
    repo.delete_menu(menu_id)
    return True

@app.post("/menu_item/", response_model=schemas.MenuItemResposne, tags=["Menu_items"])
def create_item(menu_item: schemas.CreateMenuItemDto, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    return  repo.create_menu_item(menu_item)

@app.get("/menu_items/", response_model=list[schemas.MenuItemResposne], tags=["Menu_items"])
def read_items(repo: MenuItemRepository = Depends(get_menu_item_repository)):
    menu_items = repo.get_menu_items()
    return menu_items

@app.get("/menu_items_by_menu_id/{menu_id}", response_model=list[schemas.MenuItemResposne], tags=["Menu_items"])
def read_items(menu_id: int, repo: MenuItemRepository = Depends(get_menu_item_repository)):
    menu_items = repo.get_menu_items_by_menu_id(menu_id)
    return menu_items