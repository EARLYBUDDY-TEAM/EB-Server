from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from typing import Self, Optional
from eb_fast_api.database.sources.model.base_model import Base
from eb_fast_api.database.sources.model.schedule import Schedule


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(100), primary_key=True)
    nickName: Mapped[str] = mapped_column(String(50))
    hashedPassword: Mapped[str] = mapped_column(String(60))
    scheduleTable: Mapped[str] = mapped_column(String(100))
    refreshToken: Mapped[str] = mapped_column(String(250))
    fcm_token: Mapped[Optional[str]] = mapped_column(String(250), unique=True)
    is_notify: Mapped[bool] = mapped_column(Boolean, default=True)

    def __init__(
        self,
        email: str,
        nickName: str,
        hashedPassword: str,
        refreshToken: str,
        fcm_token: Optional[str],
        is_notify: bool,
    ):
        self.email = email
        self.nickName = nickName
        self.hashedPassword = hashedPassword
        self.scheduleTable = Schedule.getTableName(email)
        self.refreshToken = refreshToken
        self.fcm_token = fcm_token
        self.is_notify = is_notify

    @classmethod
    def mock(
        cls,
        email: str = "email",
        nickName: str = "nickName",
        hashedPassword: str = "hashedPassword",
        refreshToken: str = "refreshToken",
        fcm_token: str = "fcm_token",
        is_notify: bool = True,
    ) -> Self:
        return User(
            email=email,
            nickName=nickName,
            hashedPassword=hashedPassword,
            refreshToken=refreshToken,
            fcm_token=fcm_token,
            is_notify=is_notify,
        )
