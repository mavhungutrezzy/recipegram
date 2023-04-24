from typing import List, Type

from repositories import BaseRepository

from .models import Favorite

from beanie import PydanticObjectId



class FavoriteRepository(BaseRepository):
    def __init__(self, model: Type[Favorite] = Favorite):
        super().__init__(model)

    async def add_favorite(self, new_favorite: Favorite, user: PydanticObjectId) -> Favorite:
        new_favorite.user = PydanticObjectId(user["id"])
        return await new_favorite.create()

    async def get_favorite(self, favorite_id: str) -> Favorite:
        return await Favorite.find_one(Favorite.id == favorite_id)

    async def get_favorites(self) -> List[Favorite]:
        favorites = []
        async for favorite in Favorite.find():
            favorites.append(favorite)
        return favorites

    async def update_favorite(self, favorite_id: str, favorite: Favorite) -> Favorite:
        return await Favorite.find_one_and_update(
            Favorite.id == favorite_id, favorite, return_document=True
        )

    async def delete_favorite(self, favorite_id: str) -> Favorite:
        return await self.delete(favorite_id)
    
    async def get_favorites_by_user(self, user: dict) -> List[Favorite]:
        favorites = []
        async for favorite in Favorite.find(Favorite.user == PydanticObjectId(user["id"])):
            favorites.append(favorite)
        return favorites

    async def get_favorites_by_recipe(self, recipe: str) -> List[Favorite]:
        return await Favorite.find_all(Favorite.recipe == recipe)
