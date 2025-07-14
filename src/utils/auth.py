from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from src.config.settings import settings

security = HTTPBearer()

async def verify_token(request: Request):
    credentials = await security(request)
    try:
        payload = jwt.decode(credentials.credentials, settings.JWT_SECRET, algorithms=["HS256"])
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
