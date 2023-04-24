from datetime import datetime
from beanie import Document, PydanticObjectId


class Favorite(Document):
    user: PydanticObjectId = None
    recipe: PydanticObjectId = None

    class Settings:
        collection_name = "favorites"

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
        extra_schema = {
            "example": {
                "user": "5f9a1e0d7f8b8c4f4e4b0e0d",
                "recipe": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }
