from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from api.recipe.models import Recipe
from api.user.models import User
from auth.jwt_bearer import JWTBearer

from .models import Follower, Following
from .repository import FollowerRepository, FollowingRepository
from .schemas import FollowingCreate

token_listener = JWTBearer()

router = APIRouter()


@router.get("/followers", response_model=List[Follower])
async def get_followers(user: str = Depends(token_listener)):
    return await FollowerRepository().get_followers(user)


@router.get("/following", response_model=List[Following])
async def get_following(user: str = Depends(token_listener)):
    return await FollowingRepository().get_following(user)


@router.post("/follow", response_model=Following)
async def follow_user(
    following: Following = Body(...), user: str = Depends(token_listener)
):
    following_user = await User.find_one(User.id == following.following)
    if following_user:
        return await FollowingRepository().add_following(following)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with email {following['following']} not found",
    )


@router.delete("/unfollow", response_model=dict)
async def unfollow_user(
    following: Following = Body(...), user: str = Depends(token_listener)
):
    following_id = following.id
    following = await FollowingRepository().delete_following(following_id)
    if following:
        return {"message": f"Following with id {following_id} unfollowed"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Following with id {following_id} not found",
    )


@router.get("/followers/recipes", response_model=List[Recipe])
async def get_followers_recipes(user: str = Depends(token_listener)):
    return await FollowerRepository().get_followers_recipes(user)
