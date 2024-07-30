from sqlalchemy import ForeignKey
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
    userEmail: Mapped[str] = mapped_column(ForeignKey("user.email"))
    title: Mapped[str]
    memo: Mapped[Optional[str]]
    time: Mapped[datetime]
    isNotify: Mapped[bool]
#     startPlace: Mapped[Optional["Place"]] = relationship(back_populates = "startPlace")
#     endPlace: Mapped[Optional["Place"]] = relationship(back_populates = "endPlace")

    def __eq__(self, other):
        return self.id == other.id


# # 참조카운트 0되면 삭제되게 만들기
# class Place(Base):
#     __tablename__ = "place"

#     id: Mapped[str] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     address: Mapped[str]
#     category: Mapped[str]
#     distance: Mapped[str]
#     coordiX: Mapped[str]
#     coordiY: Mapped[str]

#     startPlace: Mapped[List["Schedule"]] = relationship(back_populates = "startPlace")
#     endPlace: Mapped[List["Schedule"]] = relationship(back_populates = "endPlace")