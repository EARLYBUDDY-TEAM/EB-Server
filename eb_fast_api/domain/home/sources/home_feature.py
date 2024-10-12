from typing import List, Optional
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.domain.schema.sources.schema import PlaceInfo, ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD


def read_all_schedule(
    userEmail: str,
    scheduleCRUD: ScheduleCRUD,
) -> List[Schedule]:
    fetchedScheduleList = scheduleCRUD.read_all(userEmail=userEmail)
    return fetchedScheduleList


def get_placeinfo_from_id(
    placeID: Optional[str],
    placeCRUD: PlaceCRUD,
) -> Optional[PlaceInfo]:
    if placeID == None:
        return None
    place = placeCRUD.read(placeID=placeID)
    if place == None:
        return None
    return PlaceInfo.fromPlace(place=place)


def schedule_to_schedule_info(
    schedule: Schedule,
    placeCRUD: PlaceCRUD,
) -> ScheduleInfo:
    scheduleDict = schedule.__dict__
    id = scheduleDict["id"]
    title = scheduleDict["title"]
    memo = scheduleDict["memo"]
    time = scheduleDict["time"]
    isNotify = scheduleDict["isNotify"]

    startPlaceID = scheduleDict["startPlaceID"]
    endPlaceID = scheduleDict["endPlaceID"]
    startPlaceInfo = get_placeinfo_from_id(
        placeID=startPlaceID,
        placeCRUD=placeCRUD,
    )
    endPlaceInfo = get_placeinfo_from_id(
        placeID=endPlaceID,
        placeCRUD=placeCRUD,
    )

    return ScheduleInfo(
        id=id,
        title=title,
        memo=memo,
        time=time,
        isNotify=isNotify,
        startPlaceInfo=startPlaceInfo,
        endPlaceInfo=endPlaceInfo,
    )
