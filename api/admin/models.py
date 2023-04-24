from beanie import Document
from pydantic import EmailStr


class Admin(Document):
    fullname: str
    email: EmailStr
    password: str

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

