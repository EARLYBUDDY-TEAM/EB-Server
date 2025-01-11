from pydantic import BaseModel
from typing import Self
from eb_fast_api.domain.schema.sources.schemas import TokenInfo


class LoginResult(BaseModel):
    nick_name: str
    token_info: TokenInfo


class ChangePasswordInfo(BaseModel):
    email: str
    password: str

    @classmethod
    def mock(
        cls,
        email: str = "test@test.com",
        password: str = "test12",
    ) -> Self:
        return ChangePasswordInfo(
            email=email,
            password=password,
        )

