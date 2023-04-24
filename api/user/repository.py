from typing import Type

from repositories import BaseRepository

from .models import User


class UserRepository(BaseRepository):
    def __init__(self, model: Type[User] = User):
        super().__init__(model)

    async def add_user(self, new_user: User) -> User:
        return await new_user.create()

    async def update_user(self, user_id: str, user: User) -> User:
        return await self.update(user_id, user)

    async def delete_user(self, user_id: str) -> dict:
        return await self.delete(user_id)
