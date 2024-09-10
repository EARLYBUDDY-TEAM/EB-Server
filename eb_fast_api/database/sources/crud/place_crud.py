from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import Place


class PlaceCRUD(BaseCRUD):
    def read(self, placeID: str) -> Place:
        place = self.session.query(Place).filter(Place.id == placeID).first()
        return place

    def create(self, place: Place):
        fetchedPlace = self.read(place.id)
        if not fetchedPlace:
            self.session.add(place)
            self.session.flush()
