from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.crud.place_crud import PlaceCRUD
from eb_fast_api.database.sources.model.models import Schedule, Place, Base
from typing import Optional


class ScheduleCRUD(BaseCRUD):
    def create(
        self,
        userEmail: str,
        schedule: Schedule,
        startPlace: Optional[Place],
        endPlace: Optional[Place],
    ):
        scheduleTable = Schedule.getTable(email=userEmail)

        if startPlace is not None or endPlace is not None:
            placeCRUD = PlaceCRUD(session=self.session)
            if startPlace is not None:
                placeCRUD.create(startPlace)
            if endPlace is not None:
                placeCRUD.create(endPlace)

        stmt = scheduleTable.insert().values(
            title=schedule.title,
            time=schedule.time,
            isNotify=schedule.isNotify,
            memo=schedule.memo,
            startPlaceID=schedule.startPlaceID,
            endPlaceID=schedule.endPlaceID,
        )
        self.session.execute(stmt)
        self.session.flush()

    def dropAll(self, userEmail: str):
        self.dropTable(userEmail)
        self.removeMetaData(userEmail)

    ### Caution !!! Session Close ###
    def dropTable(self, userEmail: str):
        self.session.close()
        scheduleTable = Schedule.getTable(email=userEmail)
        scheduleTable.drop(bind=self.engine())

    def removeMetaData(self, userEmail: str):
        scheduleTable = Schedule.getTable(email=userEmail)
        Base.metadata.remove(scheduleTable)
