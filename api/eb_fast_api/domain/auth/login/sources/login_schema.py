from pydantic import BaseModel


class LoginInfo(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    email: str