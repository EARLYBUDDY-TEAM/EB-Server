from pydantic import BaseModel
from eb_fast_api.domain.schema.coordi import Coordi
from eb_fast_api.database.sources.model import Place


class PlaceInfo(BaseModel):
    id: str
    name: str
    address: str
    category: str
    distance: str
    coordi: Coordi

    def toPlace(self) -> Place:
        return Place(
            id = self.id,
            name = self.name,
            address = self.address,
            category = self.category,
            distance = self.distance,
            coordiX = self.coordi.x,
            coordiY = self.coordi.y,
        )

    @classmethod
    def mock(cls):
        return PlaceInfo(
            id = 'id',
            name = 'name',
            address = 'address',
            category = 'category',
            distance = 'distance',
            coordi=Coordi.mock(),
        )