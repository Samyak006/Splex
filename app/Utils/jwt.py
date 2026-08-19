# app/Utils/jwt_handler.py
from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "THIS_IS_THE_MOST_SAFEST_KEY_IN_THE_WORLD"  # Keep this safe!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt, expire

def decode_access_token(token: str):
    try:
        return jwt.decode(
            token,
            key=SECRET_KEY,
            algorithms=ALGORITHM
        )
    except:
        return {}

