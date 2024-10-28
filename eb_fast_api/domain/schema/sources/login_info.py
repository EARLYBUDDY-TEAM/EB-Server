from pydantic import BaseModel


class LoginInfo(BaseModel):
    email: str
    password: str
