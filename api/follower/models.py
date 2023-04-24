from datetime import datetime
from typing import List
from beanie import Document, PydanticObjectId


class Follower(Document):
    follower: PydanticObjectId = None
    following: PydanticObjectId = None

    class Settings:
        collection_name = "followers"

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
        extra_schema = {
            "example": {
                "follower": "5f9a1e0d7f8b8c4f4e4b0e0d",
                "following": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }


class Following(Document):
    follower: PydanticObjectId = None
    following: PydanticObjectId = None

    class Settings:
        collection_name = "followings"

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}
        extra_schema = {
            "example": {
                "follower": "5f9a1e0d7f8b8c4f4e4b0e0d",
                "following": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }
