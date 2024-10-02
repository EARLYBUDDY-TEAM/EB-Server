from typing import List
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD
from eb_fast_api.domain.home.sources.home_schema import ScheduleCard


def read_all_schedule(
    userEmail: str,
    scheduleCRUD: ScheduleCRUD,
) -> List[Schedule]:
    fetchedScheduleList = scheduleCRUD.read_all(userEmail=userEmail)
    return fetchedScheduleList


def schedule_to_schedulecard(
    schedule: Schedule,
    placeCRUD: PlaceCRUD,
) -> ScheduleCard:
    scheduleID = schedule.id
    title = schedule.title
    time = schedule.time

    endPlaceID = schedule.endPlaceID
    endPlace = placeCRUD.read(placeID=endPlaceID)

    return ScheduleCard(
        scheduleID=scheduleID,
        title=title,
        time=time,
        endPlaceName=endPlace.name,
    )
