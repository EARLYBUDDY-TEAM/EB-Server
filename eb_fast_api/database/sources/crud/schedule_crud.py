from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.crud.place_crud import PlaceCRUD
from eb_fast_api.database.sources.model.models import Schedule, Place, Base
from typing import Optional, List
from sqlalchemy import desc


class ScheduleCRUD(BaseCRUD):
    def create(
        self,
        userEmail: str,
        schedule: Schedule,
        startPlace: Optional[Place],
        endPlace: Optional[Place],
    ):
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine(),
        )

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

    def read_all(
        self,
        userEmail: str,
    ) -> List[dict]:
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine(),
        )
        scheduleRowList = (
            self.session.query(scheduleTable).order_by(desc(scheduleTable.c.time)).all()
        )
        return [row._mapping for row in scheduleRowList]

    def delete(
        self,
        userEmail: str,
        scheduleID: int,
    ):
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine(),
        )
        stmt = scheduleTable.delete().where(scheduleTable.c.id == scheduleID)
        self.session.execute(stmt)
        self.session.flush()

    def update(
        self,
        userEmail: str,
        schedule: Schedule,
    ):
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine(),
        )
        stmt = (
            scheduleTable.update()
            .where(scheduleTable.c.id == schedule.id)
            .values(schedule.to_dict())
        )
        self.session.execute(stmt)
        self.session.flush()

    ### Caution !!! Session Close ###
    def dropTable(
        self,
        userEmail: str,
    ):
        self.session.close()
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine(),
        )
        Base.metadata.remove(scheduleTable)
        scheduleTable.drop(bind=self.engine())
