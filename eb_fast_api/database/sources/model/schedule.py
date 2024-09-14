from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import Table
from typing import Optional, Self
from datetime import datetime
from eb_fast_api.database.sources.model.base_model import Base


class Schedule:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    memo: Mapped[Optional[str]] = mapped_column(String(200))
    time: Mapped[datetime] = mapped_column(DateTime())
    isNotify: Mapped[bool] = mapped_column(Boolean())
    startPlaceID: Mapped[Optional[str]] = mapped_column(String(200))
    endPlaceID: Mapped[Optional[str]] = mapped_column(String(200))

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

    @classmethod
    def getTableName(cls, email: str) -> str:
        return email + "_" + "schedule"

    @classmethod
    def getTable(cls, email: str) -> Table:
        scheduleTableName = Schedule.getTableName(email)
        scheduleTable = Base.metadata.tables.get(scheduleTableName)
        if scheduleTable == None:
            raise Exception(f"Not Exist Table : {scheduleTableName}")
        return scheduleTable

    @classmethod
    def addToMetaData(cls, email: str):
        tableName = Schedule.getTableName(email)

        class MixinSchedule(Schedule, Base):
            __tablename__ = tableName

            @classmethod
            def getTableName(cls) -> str:
                return cls.__table__.name

        return MixinSchedule
