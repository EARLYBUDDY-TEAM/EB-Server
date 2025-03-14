from sqlalchemy.orm import Session
from sqlalchemy import Engine
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schedule.sources.schedule_feature.create.create_schedule import (
    create_place,
)
from typing import Optional


def update_path(
    session: Session,
    engine: Engine,
    user_email: str,
    path_id: str,
    path_info: Optional[PathInfo],
):
    path_crud = EBDataBase.path.createCRUD(
        session=session,
        engine=engine,
    )
    if path_info == None:
        path_crud.delete(
            user_email=user_email,
            path_id=path_id,
        )
        return

    to_update_path = path_info.to_path(id=path_id)
    is_exist = path_crud.read(
        user_email=user_email,
        path_id=path_id,
    )
    if is_exist:
        path_crud.update(
            user_email=user_email,
            to_update_path=to_update_path,
        )
    else:
        path_crud.create(
            user_email=user_email,
            path=to_update_path,
        )


def update_my_schedule(
    session: Session,
    engine: Engine,
    user_email: str,
    schedule_info: ScheduleInfo,
) -> str:
    to_update_schedule = schedule_info.toSchedule()
    schedule_crud = EBDataBase.schedule.createCRUD(
        session=session,
        engine=engine,
    )
    schedule_crud.update(
        userEmail=user_email,
        to_update_schedule=to_update_schedule,
    )
    return to_update_schedule.id


def update_schedule(
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

    schedule_id = update_my_schedule(
        session=session,
        engine=engine,
        user_email=user_email,
        schedule_info=schedule_info,
    )

    update_path(
        session=session,
        engine=engine,
        user_email=user_email,
        path_id=schedule_id,
        path_info=path_info,
    )

    session.commit()
