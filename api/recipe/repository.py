from typing import List, Type

from repositories import BaseRepository

from .models import Recipe
from beanie import PydanticObjectId



class RecipeRepository(BaseRepository):
    def __init__(self, model: Type[Recipe] = Recipe):
        super().__init__(model)

    async def add_recipe(self, new_recipe: Recipe, author: PydanticObjectId) -> Recipe:
        new_recipe.author = author
        return await new_recipe.create()

    async def get_recipe(self, recipe_id: PydanticObjectId) -> Recipe:
        return await Recipe.find_one(Recipe.id == recipe_id)

    async def get_recipes(self) -> List[Recipe]:
        recipes = []
        async for recipe in Recipe.find():
            recipes.append(recipe)
        return recipes

    async def update_recipe(self, recipe_id: str, recipe: Recipe) -> Recipe:
        return await self.update(recipe_id, recipe)
    
    async def delete_recipe(self, recipe_id: str) -> Recipe:
        return await self.delete(recipe_id)

    async def get_recipe_by_title(self, title: str) -> Recipe:
        return await Recipe.find_one(Recipe.title == title)

    async def get_recipes_by_author(self, author: str) -> List[Recipe]:
        return await Recipe.find_all(Recipe.author == author)

    async def get_recipes_by_ingredients(self, ingredients: List[str]) -> List[Recipe]:
        return await Recipe.find_all(Recipe.ingredients == ingredients)

