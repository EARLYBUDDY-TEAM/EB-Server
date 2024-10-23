from pydantic import BaseModel
from typing import Self
from eb_fast_api.database.sources.model.models import Place
from eb_fast_api.domain.schema.sources.coordi_info import CoordiInfo


class PlaceInfo(BaseModel):
    id: str
    name: str
    address: str
    category: str
    distance: str
    coordi: CoordiInfo

    @classmethod
    def fromPlaceDict(cls, place_dict: dict) -> Self:
        return PlaceInfo(
            id=place_dict["id"],
            name=place_dict["name"],
            address=place_dict["address"],
            category=place_dict["category"],
            distance=place_dict["distance"],
            coordi=CoordiInfo(
                x=place_dict["coordiX"],
                y=place_dict["coordiY"],
            ),
        )

    def toPlace(self) -> Place:
        return Place(
            id=self.id,
            name=self.name,
            address=self.address,
            category=self.category,
            distance=self.distance,
            coordiX=self.coordi.x,
            coordiY=self.coordi.y,
        )

    @classmethod
    def mock(cls):
        return PlaceInfo(
            id="id",
            name="name",
            address="address",
            category="category",
            distance="distance",
            coordi=CoordiInfo.mock(),
        )
