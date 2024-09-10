from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List, Self
from eb_fast_api.database.sources.model.base_model import Base


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(100), primary_key=True)
    hashedPassword: Mapped[str] = mapped_column(String(60))
    schedules: Mapped[List["Schedule"]] = relationship()

    def __init__(
        self,
        email: str,
        hashedPassword: str,
    ):
        self.email = email
        self.hashedPassword = hashedPassword

    def __eq__(self, other):
        return self.email == other.email

    @classmethod
    def mock(cls, email: str = "email") -> Self:
        return User(
            email=email,
            hashedPassword="hashedPassword",
        )
