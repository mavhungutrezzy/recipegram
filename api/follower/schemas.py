from typing import List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel


class FollowerBase(BaseModel):
    follower: PydanticObjectId
    following: PydanticObjectId
    
    class Config:
        schema_extra = {
            "example": {
                "follower": "5f9a1e0d7f8b8c4f4e4b0e0d",
                "following": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }
        
        

class FollowingBase(BaseModel):
    follower: PydanticObjectId
    following: PydanticObjectId
    
    class Config:
        schema_extra = {
            "example": {
                "follower": "5f9a1e0d7f8b8c4f4e4b0e0d",
                "following": "5f9a1e0d7f8b8c4f4e4b0e0d",
            }
        }
        

class FollowerCreate(FollowerBase):
    pass


class FollowingCreate(FollowingBase):
    pass