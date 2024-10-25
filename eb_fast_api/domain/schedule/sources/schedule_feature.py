from sqlalchemy.orm import Session
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo, PlaceInfo
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional
from uuid import uuid4


def create_path(
    session: Session,
    user_email: str,
    path_id: str,
    path_info: PathInfo,
):
    path_crud = EBDataBase.path.createCRUD(session=session)
    path = path_info.to_path(id=path_id)
    path_crud.create(
        user_email=user_email,
        path=path,
    )


def update_path(
    session: Session,
    user_email: str,
    path_id: str,
    path_info: PathInfo,
):
    path_crud = EBDataBase.path.createCRUD(session=session)
    to_update_path = path_info.to_path(id=path_id)
    path_crud.update(
        user_email=user_email,
        to_update_path=to_update_path,
    )


def create_place(
    session: Session,
    place_info: Optional[PlaceInfo],
):
    place = place_info.toPlace() if place_info != None else None
    if place != None:
        placeCRUD = EBDataBase.place.createCRUD(session=session)
        placeCRUD.create(place=place)


def create_my_schedule(
    session: Session,
    user_email: str,
    schedule_id: str,
    schedule_info: ScheduleInfo,
):
    to_create_schedule = schedule_info.toSchedule(id=schedule_id)
    schedule_crud = EBDataBase.schedule.createCRUD(session=session)
    schedule_crud.create(
        userEmail=user_email,
        schedule=to_create_schedule,
    )


def create_schedule(
    session: Session,
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    pathInfo: Optional[PathInfo],
):
    create_place(
        session=session,
        place_info=scheduleInfo.startPlaceInfo,
    )
    create_place(
        session=session,
        place_info=scheduleInfo.endPlaceInfo,
    )

    schedule_id = str(uuid4())
    create_my_schedule(
        session=session,
        user_email=userEmail,
        schedule_id=schedule_id,
        schedule_info=scheduleInfo,
    )

    if pathInfo != None:
        create_path(
            session=session,
            user_email=userEmail,
            path_id=schedule_id,
            path_info=pathInfo,
        )

    session.commit()


def update_my_schedule(
    session: Session,
    user_email: str,
    schedule_info: ScheduleInfo,
) -> str:
    to_update_schedule = schedule_info.toSchedule()
    schedule_crud = EBDataBase.schedule.createCRUD(session=session)
    schedule_crud.update(
        userEmail=user_email,
        to_update_schedule=to_update_schedule,
    )
    return to_update_schedule.id


def update_schedule(
    session: Session,
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    pathInfo: Optional[PathInfo],
):
    create_place(
        session=session,
        place_info=scheduleInfo.startPlaceInfo,
    )
    create_place(
        session=session,
        place_info=scheduleInfo.endPlaceInfo,
    )

    schedule_id = update_my_schedule(
        session=session,
        user_email=userEmail,
        schedule_info=scheduleInfo,
    )

    if pathInfo != None:
        update_path(
            session=session,
            user_email=userEmail,
            path_id=schedule_id,
            path_info=pathInfo,
        )

    session.commit()
