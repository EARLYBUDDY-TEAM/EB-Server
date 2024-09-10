from sqlalchemy import ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, Self
from datetime import datetime
from eb_fast_api.database.sources.model.base import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100))
    memo: Mapped[Optional[str]] = mapped_column(String(100))
    time: Mapped[datetime] = mapped_column(DateTime())
    isNotify: Mapped[bool] = mapped_column(Boolean())
    startPlaceID: Mapped[Optional[str]] = mapped_column(String(100))
    endPlaceID: Mapped[Optional[str]] = mapped_column(String(100))

    userEmail: Mapped[str] = mapped_column(ForeignKey("user.email"))

    def __init__(
        self,
        title: str,
        time: datetime,
        isNotify: bool,
        memo: Optional[str] = None,
        startPlaceID: Optional[str] = None,
        endPlaceID: Optional[str] = None,
    ):
        self.title = title
        self.memo = memo
        self.time = time
        self.isNotify = isNotify
        self.startPlaceID = startPlaceID
        self.endPlaceID = endPlaceID

    def __eq__(self, other):
        return self.id == other.id

    @classmethod
    def mock(cls) -> Self:
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        return Schedule(
            title="title",
            memo="memo",
            time=time,
            isNotify=False,
            startPlaceID="startPlaceID",
            endPlaceID="endPlaceID",
        )
