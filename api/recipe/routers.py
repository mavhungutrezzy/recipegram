from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from auth.jwt_bearer import JWTBearer

from .models import Recipe
from .repository import RecipeRepository
from .schemas import RecipeUpdate

router = APIRouter()

token_listener = JWTBearer()


@router.get("/", response_model=List[Recipe])
async def get_recipes():
    return await RecipeRepository().get_recipes()


@router.get("/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: PydanticObjectId):
    recipe = await RecipeRepository().get_recipe(recipe_id)
    if recipe:
        return recipe
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe with id {recipe_id} not found",
    )


@router.post("/", response_model=Recipe)
async def create_recipe(
    recipe: Recipe = Body(...), author: str = Depends(token_listener)
):
    return await RecipeRepository().add_recipe(recipe, PydanticObjectId(author["id"]))


@router.put("/{recipe_id}", response_model=Recipe)
async def update_recipe(
    recipe_id: str,
    recipe: RecipeUpdate = Body(...),
    author: str = Depends(token_listener),
):
    recipe = jsonable_encoder(recipe)
    return await RecipeRepository().update_recipe(recipe_id, recipe)


@router.delete("/{recipe_id}", response_model=dict)
async def delete_recipe(recipe_id: str, author: str = Depends(token_listener)):
    recipe = await RecipeRepository().delete_recipe(recipe_id)
    if recipe:
        return JSONResponse(
            content={
                "success": True,
                "message": f"Recipe with id '{recipe_id}' was successfully deleted",
            }
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe with id {recipe_id} not found",
    )
