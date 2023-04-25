from typing import List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from fastapi.security import HTTPBasicCredentials



class UserBase(BaseModel):
    email: EmailStr = Field(..., description="The email address of the user")
    full_name: str = Field(..., description="The full name of the user")
    bio: Optional[str] = Field(None, description="The bio of the user")
    profile_pic: Optional[str] = Field(None, description="The profile picture of the user")
    followers: List[PydanticObjectId] = []
    following: List[PydanticObjectId] = []




class UserUpdate(UserBase):
    email: Optional[EmailStr]
    full_name: Optional[str]
    bio: Optional[str]
    profile_pic: Optional[str]
    followers: Optional[List[PydanticObjectId]]
    following: Optional[List[PydanticObjectId]]

    class Config:
        schema_extra = {
            "example": {
                "email": "mavhungu@gmail.com",
                "full_name": "Mavhungu",
                "bio": "I love cooking",
                "profile_pic": "https://www.profilepic.com",
            }
        }
        
        
class UserSignIn(HTTPBasicCredentials):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., description="The password of the user")

    class Config:
        schema_extra = {
            "example": {
                "email": "mavhungu@gmail.com",
                "password": "password"
            }
        }

class UserData(UserBase):
    pass