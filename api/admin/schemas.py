
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "mavhungu@edconnect.com",
                "password": "password"
            }
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Adivhaho Mavhungu",
                "email": "mavhungu@edconnect.com",
            }
        }
