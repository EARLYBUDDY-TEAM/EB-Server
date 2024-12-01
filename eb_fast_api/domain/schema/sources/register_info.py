from pydantic import BaseModel
from eb_fast_api.database.sources.model.models import User
from eb_fast_api.snippets.sources import pwdcrypt
from typing import Optional, Self


class RegisterInfo(BaseModel):
    nickName: str
    email: str
    password: str

    def toUser(
        self,
        refreshToken: str = "",
        fcm_token: Optional[str] = None,
    ) -> User:
        return User(
            email=self.email,
            nickName=self.nickName,
            hashedPassword=pwdcrypt.hash(self.password),
            refreshToken=refreshToken,
            fcm_token=fcm_token,
        )

    @classmethod
    def mock(
        cls,
        email: str = "test@test.com",
    ) -> Self:
        return RegisterInfo(
            nickName="nickName",
            email=email,
            password="password12",
        )
