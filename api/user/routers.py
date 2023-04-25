from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from passlib.context import CryptContext

from auth.jwt_bearer import JWTBearer
from auth.jwt_handler import sign_jwt

from .models import User
from .repository import UserRepository
from .schemas import UserData, UserSignIn, UserUpdate


hash_helper = CryptContext(schemes=["bcrypt"])

router = APIRouter()

token_listener = JWTBearer()


@router.post("/login")
async def user_login(user_credentials: UserSignIn = Body(...)):
    user_exists = await User.find_one(User.email == user_credentials.email)
    if user_exists:
        if password := hash_helper.verify(
            user_credentials.password, user_exists.password
        ):
            return sign_jwt(str(user_exists.id))

        raise HTTPException(status_code=403, detail="Incorrect email or password")

    raise HTTPException(status_code=403, detail="Incorrect email or password")


@router.post("/new", response_model=User)
async def user_signup(user: User = None):
    if user is None:
        user = Body(...)
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=409, detail="User with email supplied already exists"
        )

    user.password = hash_helper.encrypt(user.password)
    return await UserRepository().add_user(user)


@router.get("/me", response_model=UserData)
async def user_me(user: User = Depends(token_listener)):
    user_id = user["id"]
    user = await UserRepository().get_user_by_id(user_id)
    return user

    


@router.put("/me", response_model=User)
async def user_update_me(
    user: User = Depends(token_listener),
    user_update: UserUpdate = Body(...),
):
    user_update = jsonable_encoder(user_update)
    return await UserRepository().update_user(user["id"], user_update)



@router.delete("/me")
async def user_delete_me(user: User = Depends(token_listener)):
    user_id = user["id"]
    user = await UserRepository().delete_user(user_id)

    if user:
        return JSONResponse(
            content={
                "success": True,
                "message": "User with ID '{user_id}' was successfully deleted",
            }
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID '{user_id}' was not found",
    )


# @router.get("/{user_id}", response_model=User)