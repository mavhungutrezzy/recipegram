from fastapi import FastAPI

from api.admin.routers import router as AdminRouter
from api.favorite.routers import router as FavoriteRouter
from api.follower.routers import router as FollowerRouter
from api.recipe.routers import router as RecipeRouter
from api.user.routers import router as UserRouter
from auth.jwt_bearer import JWTBearer
from fastapi.openapi.utils import get_openapi
from config.config import close_database, initiate_database

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.on_event("shutdown")
async def close_database():
    await close_database()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="RecipeGram API",
        version="1.0.0",
        description="Recipe API",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(RecipeRouter, tags=["Recipe"], prefix="/recipe")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(FavoriteRouter, tags=["Favorite"], prefix="/favorites")
app.include_router(FollowerRouter, tags=["Follower"], prefix="/follower")
