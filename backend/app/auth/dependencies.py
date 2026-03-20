from fastapi import Depends, HTTPException, Header
from app.auth.jwt_handler import decode_token

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        token = authorization.split(" ")[1]
        payload = decode_token(token)
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


def require_admin(user=Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user
