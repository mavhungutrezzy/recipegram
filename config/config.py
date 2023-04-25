from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from api.admin.models import Admin
from api.favorite.models import Favorite
from api.follower.models import Follower, Following
from api.recipe.models import Recipe
from api.user.models import User


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None
    CORS_ORIGINS: Optional[str] = None

    # JWT
    secret_key: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[Admin, Recipe, User, Favorite, Follower, Following],
    )


async def close_database():
    await init_beanie().close()
