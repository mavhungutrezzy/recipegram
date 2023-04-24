from beanie import PydanticObjectId
from pydantic import BaseModel


class FavoriteBase(BaseModel):
    user: PydanticObjectId
    recipe: PydanticObjectId

    class Config:
        schema_extra = {
            "example": {
                "user": "5f9a1e0d7f8b8c4f4e4b0e0d",
                "recipe": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }
        

class FavoriteCreate(FavoriteBase):
    pass