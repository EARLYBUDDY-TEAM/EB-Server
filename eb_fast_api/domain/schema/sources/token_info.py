from pydantic import BaseModel


class TokenInfo(BaseModel):
    accessToken: str
    refreshToken: str
