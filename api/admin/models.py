from beanie import Document
from pydantic import EmailStr, Field


class Admin(Document):
    fullname: str = Field(..., description="The full name of the admin")
    email: EmailStr = Field(..., description="The email address of the admin")
    password: str = Field(..., description="The password of the admin")

    class Settings:
        name = "admin"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Adivhaho Mavhungu",
                "email": "mavhungu@edconnect.com",
                "password": "password"
            }
        }

