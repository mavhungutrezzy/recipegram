from datetime import datetime
from typing import List
from beanie import Document, PydanticObjectId
from pydantic import Field


class Recipe(Document):
    title: str = Field(..., description="The title of the recipe")
    description: str = Field(..., description="The description of the recipe")
    ingredients: List[str] = Field(..., description="The ingredients of the recipe")
    instructions: List[str] = Field(..., description="The instructions of the recipe")
    created_at: datetime = datetime.now() 
    author: PydanticObjectId = None

    class Settings:
        collection_name = "recipes"

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
        extra_schema = {
            "example": {
                "title": "Pancakes",
                "description": "A pancake is a flat cake, often thin and round, prepared from a starch-based batter that may contain eggs, milk and butter and cooked on a hot surface such as a griddle or frying pan, often frying with oil or butter.",
                "ingredients": [
                    "1 cup all-purpose flour",
                    "1 tablespoon white sugar",
                    "1 teaspoon baking powder",
                    "1/2 teaspoon salt",
                    "1 egg",
                    "1 cup milk",
                    "3 tablespoons butter, melted",
                ],
                "instructions": [
                    "In a large bowl, sift together the flour, sugar, baking powder and salt. Make a well in the center and pour in the egg, milk and melted butter; mix until smooth.",
                    "Heat a lightly oiled griddle or frying pan over medium high heat. Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake. Brown on both sides and serve hot.",
                ],
                "author": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }
