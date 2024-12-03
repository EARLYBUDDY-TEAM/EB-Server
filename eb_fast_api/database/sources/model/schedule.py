from sqlalchemy import String, DateTime, Engine, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import Table, MetaData
from typing import Optional, Self
from datetime import datetime
from eb_fast_api.database.sources.model.base_model import Base
from eb_fast_api.database.sources.connection import engine
from uuid import uuid4
from eb_fast_api.snippets.testings.mock_eb_datetime import mock_now 


class Schedule:
    id = Column(String(50), primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    memo: Mapped[Optional[str]] = mapped_column(String(200))
    time: Mapped[datetime] = mapped_column(DateTime())
    notify_schedule: Mapped[Optional[int]] = mapped_column(Integer())
    notify_transport: Mapped[Optional[int]] = mapped_column(Integer())
    notify_transport_range: Mapped[Optional[int]] = mapped_column(Integer())
    startPlaceID: Mapped[Optional[str]] = mapped_column(String(200))
    endPlaceID: Mapped[Optional[str]] = mapped_column(String(200))

    def __init__(
        self,
        title: str,
        time: datetime,
        notify_schedule: Optional[int] = None,
        notify_transport: Optional[int] = None,
        notify_transport_range: Optional[int] = None,
        memo: Optional[str] = None,
        startPlaceID: Optional[str] = None,
        endPlaceID: Optional[str] = None,
        id: str = str(uuid4()),
    ):
        self.id = id
        self.title = title
        self.memo = memo
        self.time = time.replace(microsecond=0, tzinfo=None)
        self.notify_schedule = notify_schedule
        self.notify_transport = notify_transport
        self.notify_transport_range = notify_transport_range
        self.startPlaceID = startPlaceID
        self.endPlaceID = endPlaceID

    @classmethod
    def mock(
        cls,
        id: Optional[str] = None,
        title: str = "title",
        time: datetime = mock_now,
    ) -> Self:
        id = id or str(uuid4())
        mockSchedule = Schedule(
            id=id,
            title=title,
            memo="memo",
            time=time,
            notify_schedule=10,
            notify_transport=10,
            notify_transport_range=10,
            startPlaceID="startPlaceID",
            endPlaceID="endPlaceID",
        )
        return mockSchedule

    @classmethod
    def getTableName(cls, email: str) -> str:
        return email + "_" + "schedule"

    @classmethod
    def getTable(
        cls,
        email: str,
        engine: Engine = engine,
    ) -> Table:
        scheduleTableName = Schedule.getTableName(email)
        scheduleMetaData = MetaData()
        scheduleMetaData.reflect(
            bind=engine,
            only=[scheduleTableName],
        )
        scheduleTable = scheduleMetaData.tables.get(scheduleTableName)
        if scheduleTable == None:
            raise Exception(f"No Exist Table : {scheduleTableName}")
        return scheduleTable

    @classmethod
    def createMixinSchedule(cls, email: str):
        tableName = Schedule.getTableName(email)

        class MixinSchedule(Schedule, Base):
            __tablename__ = tableName

            @classmethod
            def getTableName(cls) -> str:
                return cls.__table__.name

        return MixinSchedule

    def to_dict(self, id: Optional[str] = None) -> dict:
        return {
            "id": id or self.id,
            "title": self.title,
            "memo": self.memo,
            "time": self.time,
            "notify_schedule": self.notify_schedule,
            "notify_transport": self.notify_transport,
            "notify_transport_range": self.notify_transport_range,
            "startPlaceID": self.startPlaceID,
            "endPlaceID": self.endPlaceID,
        }
