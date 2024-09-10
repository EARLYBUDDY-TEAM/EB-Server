from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.crud.place_crud import PlaceCRUD
from eb_fast_api.database.sources.model.models import Schedule, Place, User
from typing import Optional


class ScheduleCRUD(BaseCRUD):
    def create(
        self,
        userEmail: str,
        schedule: Schedule,
        startPlace: Optional[Place],
        endPlace: Optional[Place],
    ):
        user = self.session.query(User).filter(User.email == userEmail).first()
        if not user:
            raise Exception("no user")

        if startPlace is not None or endPlace is not None:
            placeCRUD = PlaceCRUD(session=self.session)
            if startPlace is not None:
                placeCRUD.create(startPlace)
            if endPlace is not None:
                placeCRUD.create(endPlace)

        user.schedules.append(schedule)  # 중복체크?
        self.session.flush()
