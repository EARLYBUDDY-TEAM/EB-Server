from pydantic import BaseModel
from typing import Self


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

