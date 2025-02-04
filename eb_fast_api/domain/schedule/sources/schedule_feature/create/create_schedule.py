from sqlalchemy.orm import Session
from sqlalchemy import Engine
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo, PlaceInfo
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional


def create_path(
    session: Session,
    engine: Engine,
    user_email: str,
    path_id: str,
    path_info: PathInfo,
):
    path_crud = EBDataBase.path.createCRUD(
        session=session,
        engine=engine,
    )
    path = path_info.to_path(id=path_id)
    path_crud.create(
        user_email=user_email,
        path=path,
    )


def create_place(
    session: Session,
    engine: Engine,
    place_info: Optional[PlaceInfo],
):
    place = place_info.toPlace() if place_info != None else None
    if place != None:
        placeCRUD = EBDataBase.place.createCRUD(
            session=session,
            engine=engine,
        )
        placeCRUD.create(place=place)


def create_my_schedule(
    session: Session,
    engine: Engine,
    user_email: str,
    schedule_info: ScheduleInfo,
):
    to_create_schedule = schedule_info.toSchedule()
    schedule_crud = EBDataBase.schedule.createCRUD(
        session=session,
        engine=engine,
    )
    schedule_crud.create(
        userEmail=user_email,
        schedule=to_create_schedule,
    )


def create_schedule(
    session: Session,
    engine: Engine,
    user_email: str,
    schedule_info: ScheduleInfo,
    path_info: Optional[PathInfo],
):
    create_place(
        session=session,
        engine=engine,
        place_info=schedule_info.startPlaceInfo,
    )
    create_place(
        session=session,
        engine=engine,
        place_info=schedule_info.endPlaceInfo,
    )

    create_my_schedule(
        session=session,
        engine=engine,
        user_email=user_email,
        schedule_info=schedule_info,
    )

    if path_info != None:
        create_path(
            session=session,
            engine=engine,
            user_email=user_email,
            path_id=schedule_info.id,
            path_info=path_info,
        )

    session.commit()
