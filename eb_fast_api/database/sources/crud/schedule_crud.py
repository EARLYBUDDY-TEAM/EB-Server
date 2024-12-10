from eb_fast_api.database.sources.crud.base_crud import BaseCRUD
from eb_fast_api.database.sources.model.models import Schedule
from typing import List
from sqlalchemy import desc, asc


class ScheduleCRUD(BaseCRUD):
    def create(
        self,
        userEmail: str,
        schedule: Schedule,
    ):
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine,
        )

        stmt = scheduleTable.insert().values(schedule.to_dict())
        self.session.execute(stmt)
        self.session.flush()

    def read(
        self,
        user_email: str,
        schedule_id: str,
    ) -> dict:
        scheduleTable = Schedule.getTable(
            email=user_email,
            engine=self.engine,
        )
        schedule_row = (
            self.session.query(scheduleTable)
            .filter(scheduleTable.c.id == schedule_id)
            .one()
        )

        return schedule_row._mapping

    def read_all(
        self,
        userEmail: str,
    ) -> List[dict]:
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine,
        )
        scheduleRowList = (
            self.session.query(scheduleTable).order_by(asc(scheduleTable.c.time)).all()
        )
        return [row._mapping for row in scheduleRowList]

    def delete(
        self,
        userEmail: str,
        scheduleID: str,
    ):
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine,
        )
        stmt = scheduleTable.delete().where(scheduleTable.c.id == scheduleID)
        self.session.execute(stmt)
        self.session.flush()

    def update(
        self,
        userEmail: str,
        to_update_schedule: Schedule,
    ):
        scheduleTable = Schedule.getTable(
            email=userEmail,
            engine=self.engine,
        )
        stmt = (
            scheduleTable.update()
            .where(scheduleTable.c.id == to_update_schedule.id)
            .values(to_update_schedule.to_dict())
        )
        self.session.execute(stmt)
        self.session.flush()
