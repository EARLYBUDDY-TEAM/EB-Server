from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self
from eb_fast_api.database.sources.model.base_model import Base


# 참조카운트 0되면 삭제되게 만들기
class Place(Base):
    __tablename__ = "place"

    id: Mapped[str] = mapped_column(String(200), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    address: Mapped[str] = mapped_column(String(200))
    category: Mapped[str] = mapped_column(String(200))
    distance: Mapped[str] = mapped_column(String(200))
    coordiX: Mapped[str] = mapped_column(String(200))
    coordiY: Mapped[str] = mapped_column(String(200))

    refCount = Column(Integer, default=0)

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

    @classmethod
    def mockEnd(cls) -> Self:
        return Place(
            id="2140311573",
            name="스타벅스 수서역R점",
            address="서울 강남구 광평로 281",
            category="카페",
            distance="0.1",
            coordiX="127.10297988971773",
            coordiY="37.48800665367514",
        )

    @classmethod
    def mockStart(cls) -> Self:
        return Place(
            id="123",
            name="멜로즈",
            address="서울 용산구 보광로 82",
            category="카페",
            distance="12",
            coordiX="126.996509759576",
            coordiY="37.5306176474415",
        )
