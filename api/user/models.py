from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import EmailStr


class User(Document):
    email: EmailStr
    password: str
    full_name: str
    bio: Optional[str]
    profile_pic: Optional[str]
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