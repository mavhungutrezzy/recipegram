from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from api.recipe.models import Recipe
from auth.jwt_bearer import JWTBearer
from beanie import PydanticObjectId

from .models import Favorite
from .repository import FavoriteRepository
from .schemas import FavoriteCreate

token_listener = JWTBearer()

router = APIRouter()


@router.post("/favorite", response_model=Favorite)
async def favorite_recipe(
    favorite: Favorite = Body(...), user: str = Depends(token_listener)
):
    recipe = await Recipe.find_one(Recipe.id == PydanticObjectId(favorite.recipe))
    if recipe:
        return await FavoriteRepository().add_favorite(favorite, user)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Recipe with id {favorite.recipe} not found",
    )


@router.delete("/unfavorite", response_model=dict)
async def unfavorite_recipe(
    favorite: Favorite = Body(...), user: str = Depends(token_listener)
):
    favorite_id = favorite.id
    recipe = await FavoriteRepository().delete_favorite(favorite_id)
    if recipe:
        return {"message": f"Favorite recipe with id {favorite_id} deleted"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Favorite recipe with id {favorite_id} not found",
    )


@router.get("/favorites", response_model=List[Favorite])
async def get_favorites(user: str = Depends(token_listener)):
    return await FavoriteRepository().get_favorites_by_user(user)
