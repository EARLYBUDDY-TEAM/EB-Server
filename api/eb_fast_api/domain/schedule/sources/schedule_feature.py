from eb_fast_api.domain.schedule.sources.schedule_schema import ScheduleInfo
from eb_fast_api.database.sources.models import Schedule
from eb_fast_api.database.sources import db_crud

def create_schedule(userEmail: str, scheduleInfo: ScheduleInfo):
    # startPlaceID = (
    #     scheduleInfo.startPlace.id if scheduleInfo.startPlace != None else None
    # )
    # endPlaceID = scheduleInfo.endPlace.id if scheduleInfo.endPlace != None else None


    schedule = Schedule(
        title=scheduleInfo.title,
        memo=scheduleInfo.memo,
        time=scheduleInfo.time,
        isNotify=scheduleInfo.isNotify,
    )

    if scheduleInfo.startPlace is not None:
        schedule.startPlaceID = scheduleInfo.startPlace.id
        ## 

    if scheduleInfo.endPlace is not None:
        schedule.endPlaceID = scheduleInfo.endPlace.id


    schedule = Schedule(
        title=scheduleInfo.title,
        memo=scheduleInfo.memo,
        time=scheduleInfo.time,
        isNotify=scheduleInfo.isNotify,
    )
    db_crud.schedule_create(userEmail, schedule)
