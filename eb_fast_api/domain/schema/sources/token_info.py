from pydantic import BaseModel
from typing import Self


class TokenInfo(BaseModel):
    accessToken: str
    refreshToken: str

    @classmethod
    def mock(cls) -> Self:
        return cls(
            accessToken="accessToken",
            refreshToken="refreshToken",
        )
