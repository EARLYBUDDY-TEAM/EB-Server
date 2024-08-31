from pydantic import BaseModel


class Token(BaseModel):
    accessToken: str
    refreshToken: str

    def __init__(
        self,
        accessToken: str,
        refreshToken: str,
    ):
        super().__init__(
            accessToken=accessToken,
            refreshToken=refreshToken,
        )