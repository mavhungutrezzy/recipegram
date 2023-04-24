from fastapi import FastAPI

from api.admin.routers import router as AdminRouter
from api.favorite.routers import router as FavoriteRouter
from api.follower.routers import router as FollowerRouter
from api.recipe.routers import router as RecipeRouter
from api.user.routers import router as UserRouter
from auth.jwt_bearer import JWTBearer
from config.config import close_database, initiate_database

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.on_event("shutdown")
async def close_database():
    await close_database()


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(RecipeRouter, tags=["Recipe"], prefix="/recipe")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(FavoriteRouter, tags=["Favorite"], prefix="/favorites")
app.include_router(FollowerRouter, tags=["Follower"], prefix="/follower")
