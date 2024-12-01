from pydantic import BaseModel
from typing import Self


class LoginInfo(BaseModel):
    email: str
    password: str
    fcm_token: str

    @classmethod
    def mock(cls) -> Self:
        return LoginInfo(
            email="email",
            password="password",
            fcm_token="fcm_token",
        )
