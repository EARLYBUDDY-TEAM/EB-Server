from sqlalchemy.orm import Session
from sqlalchemy import Engine
from eb_fast_api.database.sources.database import EBDataBase


def delete_schedule(
    session: Session,
    user_email: str,
    schedule_id: str,
    engine: Engine,
):
    scheduleCRUD = EBDataBase.schedule.createCRUD(
        session=session,
        engine=engine,
    )
    scheduleCRUD.delete(
        userEmail=user_email,
        scheduleID=schedule_id,
    )
    pathCRUD = EBDataBase.path.createCRUD(
        session=session,
        engine=engine,
    )
    pathCRUD.delete(
        user_email=user_email,
        path_id=schedule_id,
    )
    session.commit()
