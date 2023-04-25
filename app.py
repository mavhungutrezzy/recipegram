from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from api.admin.routers import router as AdminRouter
from api.favorite.routers import router as FavoriteRouter
from api.follower.routers import router as FollowerRouter
from api.recipe.routers import router as RecipeRouter
from api.user.routers import router as UserRouter
from auth.jwt_bearer import JWTBearer
from config.config import Settings, close_database, initiate_database

token_listener = JWTBearer()


app = FastAPI()


origins = Settings().CORS_ORIGINS.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        description="RecipeGram API is a RESTful API built with [FastAPI](https://fastapi.tiangolo.com/) and [MongoDB](https://www.mongodb.com/) using [Beanie](https://beanie-odm.dev/) as an ODM. It provides endpoints for performing CRUD operations on recipes, following recipe authors, viewing recipes by author, and adding recipes to favorites. It also provides endpoints for registering and authenticating users, and for managing users and recipes as an administrator. The API is secured with [JWT](https://jwt.io/) authentication",
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
