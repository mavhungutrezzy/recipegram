from typing import List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr
from fastapi.security import HTTPBasicCredentials



class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    bio: Optional[str]
    profile_pic: Optional[str]
    followers: List[PydanticObjectId] = []
    following: List[PydanticObjectId] = []


class UserCreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "mavhungu@recipegram.com",
                "full_name": "Mavhungu",
                "password": "password",
            }
        }


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
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "mavhungu@gmail.com",
                "password": "password"
            }
        }
