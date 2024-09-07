from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Engine
from eb_fast_api.database.sources.database import engine
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from typing import Optional, List, Self
from datetime import datetime


Base = declarative_base()


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


# 참조카운트 0되면 삭제되게 만들기
class Place(Base):
    __tablename__ = "place"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(100))
    distance: Mapped[str] = mapped_column(String(100))
    coordiX: Mapped[str] = mapped_column(String(100))
    coordiY: Mapped[str] = mapped_column(String(100))

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
    def mock(cls, id: str = "id") -> Self:
        return Place(
            id=id,
            name="name",
            address="address",
            category="category",
            distance="distance",
            coordiX="coordiX",
            coordiY="coordiY",
        )


def createTable(engine: Engine = engine):
    Base.metadata.create_all(bind=engine)


def dropTable(engine: Engine = engine):
    Base.metadata.drop_all(bind=engine)
