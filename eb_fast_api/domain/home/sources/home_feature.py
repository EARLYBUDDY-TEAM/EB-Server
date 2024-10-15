from typing import List, Optional
from eb_fast_api.domain.schema.sources.schema import PlaceInfo, ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD


def read_all_schedule(
    userEmail: str,
    scheduleCRUD: ScheduleCRUD,
) -> List[dict]:
    fetched_schedule_dict_list = scheduleCRUD.read_all(userEmail=userEmail)
    return fetched_schedule_dict_list


def get_placeinfo_from_id(
    placeID: Optional[str],
    placeCRUD: PlaceCRUD,
) -> Optional[PlaceInfo]:
    if placeID == None:
        return None
    place_dict = placeCRUD.read(place_id=placeID)
    if place_dict == None:
        return None
    return PlaceInfo.fromPlaceDict(place_dict=place_dict)


def schedule_dict_to_schedule_info(
    schedule_dict: dict,
    placeCRUD: PlaceCRUD,
) -> ScheduleInfo:
    id = schedule_dict["id"]
    title = schedule_dict["title"]
    memo = schedule_dict["memo"]
    time = schedule_dict["time"]
    isNotify = schedule_dict["isNotify"]

    startPlaceID = schedule_dict["startPlaceID"]
    endPlaceID = schedule_dict["endPlaceID"]
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
