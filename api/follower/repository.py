
from typing import List, Type

from repositories import BaseRepository

from .models import Follower, Following
from api.recipe.models import Recipe


class FollowerRepository(BaseRepository):
    def __init__(self, model: Type[Follower] = Follower):
        super().__init__(model)

    async def add_follower(self, new_follower: Follower) -> Follower:
        return await new_follower.create()

    async def get_follower(self, follower_id: str) -> Follower:
        return await Follower.find_one(Follower.id == follower_id)

    async def get_followers(self, user: str) -> List[Follower]:
        followers = []
        async for follower in Follower.find():
            followers.append(follower)
        return followers

    async def update_follower(self, follower_id: str, follower: Follower) -> Follower:
        return await Follower.find_one_and_update(
            Follower.id == follower_id, follower, return_document=True
        )

    async def delete_follower(self, follower_id: str) -> Follower:
        return await Follower.find_one_and_delete(Follower.id == follower_id)

    async def get_followers_by_user(self, user: str) -> List[Follower]:
        return await Follower.find_all(Follower.user == user)

    async def get_followers_by_follower(self, follower: str) -> List[Follower]:
        return await Follower.find_all(Follower.follower == follower)
    
    async def get_followers_recipes(self, user: str) -> List[Recipe]:
        recipes = []
        async for follower in Follower.find_all(Follower.follower == user["id"]):
            async for recipe in Recipe.find_all(Recipe.author == follower.follower):
                recipes.append(recipe)
        return recipes



class FollowingRepository(BaseRepository):
    def __init__(self, model: Type[Following] = Following):
        super().__init__(model)

    async def add_following(self, new_following: Following) -> Following:
        return await new_following.create()

    async def get_following(self, following_id: str) -> Following:
        return await Following.find_one(Following.id == following_id)

    async def get_followings(self) -> List[Following]:
        followings = []
        async for following in Following.find():
            followings.append(following)
        return followings

    async def update_following(
        self, following_id: str, following: Following
    ) -> Following:
        return await Following.find_one_and_update(
            Following.id == following_id, following, return_document=True
        )

    async def delete_following(self, following_id: str) -> Following:
        return await self.delete(following_id)

    async def get_followings_by_user(self, user: str) -> List[Following]:
        return await Following.find_all(Following.user == user)

    async def get_followings_by_following(self, following: str) -> List[Following]:
        return await Following.find_all(Following.following == following)

