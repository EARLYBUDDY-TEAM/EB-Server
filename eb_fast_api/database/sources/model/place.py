from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self
from eb_fast_api.database.sources.model.base_model import Base


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
