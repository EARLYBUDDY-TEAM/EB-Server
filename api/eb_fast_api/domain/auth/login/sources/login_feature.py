from datetime import datetime, timedelta
from jose import jwt
import secrets


ACCESS_TOKEN_EXPIRE_MINUTES = 10
SECRET_KEY = secrets.token_hex(32)


# def createToken(email: str) -> str:
#     data = {
#         "sub": email,
#         "exp" : datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     }
#     accessToken = jwt.encode(data, SECRET_KEY)
#     return accessToken