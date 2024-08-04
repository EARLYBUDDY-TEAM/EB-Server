from pydantic import BaseModel
from eb_fast_api.database.sources.model import User
from eb_fast_api.snippets.sources import pwdcrypt


class UserInfo(BaseModel):
    email: str
    password: str

    def __init__(self, email: str, password: str):
        super().__init__(email = email, password = password)

    def toUser(self) -> User:
        return User(
            email=self.email,
            hashedPassword=pwdcrypt.hash(self.password),
        )
