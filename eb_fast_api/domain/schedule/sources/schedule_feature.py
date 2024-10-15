from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def createSchedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    schedule = scheduleInfo.toSchedule()
    startPlace = (
        scheduleInfo.startPlaceInfo.toPlace()
        if scheduleInfo.startPlaceInfo != None
        else None
    )
    endPlace = (
        scheduleInfo.endPlaceInfo.toPlace()
        if scheduleInfo.endPlaceInfo != None
        else None
    )

    scheduleCRUD.create(
        userEmail,
        schedule,
        startPlace,
        endPlace,
    )
