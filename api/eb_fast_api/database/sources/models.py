from sqlalchemy import Column, ForeignKey, Integer
from eb_fast_api.database.sources.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List, Self
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
    schedules: Mapped[List["Schedule"]] = relationship()

    def __init__(
        self,
        email: str,
        password: str,
    ):
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.email == other.email

    @classmethod
    def mock(cls, email: str = 'email') -> Self:
        return User(
            email=email,
            password="password",
        )


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    memo: Mapped[Optional[str]]
    time: Mapped[datetime]
    isNotify: Mapped[bool]
    startPlaceID: Mapped[Optional[str]]
    endPlaceID: Mapped[Optional[str]]

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


# 참조카운트 0되면 삭제되게 만들기
class Place(Base):
    __tablename__ = "place"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    category: Mapped[str]
    distance: Mapped[str]
    coordiX: Mapped[str]
    coordiY: Mapped[str]

    refCount = Column(Integer, default=0)

    def __eq__(self, other):
        return self.id == other.id

    def __init__(
        self,
        id: str,
        name: str,
        address: str,
        category: str,
        distance: str,
        coordiX: str,
        coordiY: str,
    ):
        self.id = id
        self.name = name
        self.address = address
        self.category = category
        self.distance = distance
        self.coordiX = coordiX
        self.coordiY = coordiY

    @classmethod
    def mock(cls, id: str = 'id') -> Self:
        return Place(
            id=id,
            name="name",
            address="address",
            category="category",
            distance="distance",
            coordiX="coordiX",
            coordiY="coordiY",
        )
