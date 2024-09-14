from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from typing import Self
from eb_fast_api.database.sources.model.base_model import Base
from eb_fast_api.database.sources.model.schedule import Schedule


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(100), primary_key=True)
    hashedPassword: Mapped[str] = mapped_column(String(60))
    scheduleTable: Mapped[str] = mapped_column(String(100))

    def __init__(
        self,
        email: str,
        hashedPassword: str,
    ):
        self.email = email
        self.hashedPassword = hashedPassword
        self.scheduleTable = Schedule.getTableName(email)

    def __eq__(self, other):
        return self.email == other.email

    @classmethod
    def mock(cls, email: str = "email") -> Self:
        return User(
            email=email,
            hashedPassword="hashedPassword",
        )
