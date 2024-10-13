from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import Place
from typing import Optional


class PlaceCRUD(BaseCRUD):
    def read(self, place_id: str) -> Optional[dict]:
        try:
            place = self.session.query(Place).filter(Place.id == place_id).one()
            return place.to_dict()
        except:
            return None

    def create(self, place: Place):
        fetched_place = self.read(place.id)
        if not fetched_place:
            self.session.add(place)
            self.session.flush()
