from pydantic import BaseModel


class Token(BaseModel):
    accessToken: str
    refreshToken: str

    def __init__(
        self,
        accessToken: str,
        refreshToken: str,
    ):
        self.accessToken = accessToken
        self.refreshToken = refreshToken