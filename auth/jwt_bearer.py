from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .jwt_handler import decode_jwt


def verify_jwt(jwtoken: str) -> bool:
    payload = decode_jwt(jwtoken)
    return bool(payload)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        print("Credentials :", credentials)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization token")
        if credentials.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication token")

        if not verify_jwt(credentials.credentials):
            raise HTTPException(
                status_code=403, detail="Invalid token or expired token"
            )

        return decode_jwt(credentials.credentials)
