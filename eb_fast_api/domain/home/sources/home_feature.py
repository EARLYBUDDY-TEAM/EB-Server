from sqlalchemy.orm import Session
from typing import List, Optional

from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.domain.schema.sources.schemas import PlaceInfo, ScheduleInfo, PathInfo
from eb_fast_api.domain.home.sources.home_schema import SchedulePathInfo


def read_all_schedule(
    userEmail: str,
    session: Session,
) -> List[dict]:
    scheduleCRUD = EBDataBase.schedule.createCRUD(session=session)
    fetched_schedule_dict_list = scheduleCRUD.read_all(userEmail=userEmail)
    return fetched_schedule_dict_list


def get_placeinfo_from_id(
    placeID: Optional[str],
    session: Session,
) -> Optional[PlaceInfo]:
    if placeID == None:
        return None
    placeCRUD = EBDataBase.place.createCRUD(session=session)
    place_dict = placeCRUD.read(place_id=placeID)
    if place_dict == None:
        return None
    return PlaceInfo.fromPlaceDict(place_dict=place_dict)


def get_schedule_info_from_dict(
    session: Session,
    schedule_dict: dict,
) -> ScheduleInfo:
    id = schedule_dict["id"]
    title = schedule_dict["title"]
    memo = schedule_dict["memo"]
    time = schedule_dict["time"]
    notify_schedule = schedule_dict["notify_schedule"]
    notify_transport = schedule_dict["notify_transport"]
    notify_transport_range = schedule_dict["notify_transport_range"]

    startPlaceID = schedule_dict["startPlaceID"]
    endPlaceID = schedule_dict["endPlaceID"]
    startPlaceInfo = get_placeinfo_from_id(
        session=session,
        placeID=startPlaceID,
    )
    endPlaceInfo = get_placeinfo_from_id(
        session=session,
        placeID=endPlaceID,
    )

    return ScheduleInfo(
        id=id,
        title=title,
        memo=memo,
        time=time,
        notify_schedule=notify_schedule,
        notify_transport=notify_transport,
        notify_transport_range=notify_transport_range,
        startPlaceInfo=startPlaceInfo,
        endPlaceInfo=endPlaceInfo,
    )


def get_path_info(
    session: Session,
    user_email: str,
    schedule_id: str,
) -> Optional[PathInfo]:
    pathCRUD = EBDataBase.path.createCRUD(session=session)
    path_dict = pathCRUD.read(
        user_email=user_email,
        path_id=schedule_id,
    )

    if path_dict == None:
        return None
    
    path_info_dict = path_dict["data"]
    path_info = PathInfo.model_validate(path_info_dict)
    return path_info


def schedule_dict_to_schedule_path_info(
    session: Session,
    user_email: str,
    schedule_dict: dict,
) -> SchedulePathInfo:
    schedule_info = get_schedule_info_from_dict(
        session=session,
        schedule_dict=schedule_dict,
    )

    schedule_id = schedule_info.id
    path_info = get_path_info(
        session=session,
        user_email=user_email,
        schedule_id=schedule_id,
    )

    return SchedulePathInfo(
        schedule_info=schedule_info,
        path_info=path_info,
    )
