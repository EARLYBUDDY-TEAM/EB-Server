from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def createSchedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    schedule = scheduleInfo.toSchedule()
    startPlace = (
        scheduleInfo.startPlace.toPlace() if scheduleInfo.startPlace != None else None
    )
    endPlace = (
        scheduleInfo.endPlace.toPlace() if scheduleInfo.endPlace != None else None
    )

    scheduleCRUD.create(
        userEmail,
        schedule,
        startPlace,
        endPlace,
    )
