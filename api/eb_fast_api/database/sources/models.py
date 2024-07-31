from sqlalchemy import Column, ForeignKey, Integer
from eb_fast_api.database.sources.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(primary_key = True)
    password: Mapped[str]
    schedules: Mapped[List["Schedule"]] = relationship()

    def __eq__(self, other):
        return self.email == other.email


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

    def __eq__(self, other):
        return self.id == other.id


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

    refCount = Column(Integer, default = 0)

    def __eq__(self, other):
        return self.id == other.id