from pydantic import BaseModel
from eb_fast_api.database.sources.model.models import User
from eb_fast_api.snippets.sources import pwdcrypt


class RegisterInfo(BaseModel):
    nickName: str
    email: str
    password: str

    def toUser(self, refreshToken: str) -> User:
        return User(
            email=self.email,
            nickName=self.nickName,
            hashedPassword=pwdcrypt.hash(self.password),
            refreshToken=refreshToken,
        )
