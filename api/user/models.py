from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import EmailStr, Field


class User(Document):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., description="The password of the user")
    full_name: str = Field(..., description="The full name of the user")
    bio: Optional[str] = Field(None, description="The bio of the user")
    profile_pic: Optional[str] = Field(None, description="The profile picture of the user")
    followers: List[PydanticObjectId] = []
    following: List[PydanticObjectId] = []

    class Settings:
        collection_name = "users"
        
    
    class Config:
        schema_extra = {
            "example": {
                "email": "mavhungu@gmail.com",
                "full_name": "Mavhungu",
                "password": "password",
                "bio": "I love cooking",
                "profile_pic": "https://www.profilepic.com",
                "follower": [],
                "following": []
            
            }
        }