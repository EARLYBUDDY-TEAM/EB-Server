from datetime import datetime, timedelta
from jose import jwt
import secrets

ACCESS_TOKEN_EXPIRE_MINUTES = 10
SECRET_KEY = secrets.token_hex(32)

def create_token(email: str) -> str:
    data = {
        "sub": email,
        "exp" : datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY)
    return access_token