from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from typing import Self
from eb_fast_api.database.sources.model.base_model import Base
from eb_fast_api.database.sources.model.schedule import Schedule


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    hashedPassword: Mapped[str] = mapped_column(String(60))
    scheduleTable: Mapped[str] = mapped_column(String(100))
    refreshToken: Mapped[str] = mapped_column(String(250))

    def __init__(
        self,
        email: str,
        name: str,
        hashedPassword: str,
        refreshToken: str,
    ):
        self.email = email
        self.name = name
        self.hashedPassword = hashedPassword
        self.scheduleTable = Schedule.getTableName(email)
        self.refreshToken = refreshToken

    @classmethod
    def mock(
        cls,
        email: str = "email",
        name: str = "name",
        hashedPassword: str = "hashedPassword",
        refreshToken: str = "refreshToken",
    ) -> Self:
        return User(
            email=email,
            name=name,
            hashedPassword=hashedPassword,
            refreshToken=refreshToken,
        )
