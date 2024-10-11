from eb_fast_api.domain.schedule.sources.schedule_schema import AddScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def createSchedule(
    userEmail: str,
    addScheduleInfo: AddScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
    schedule = addScheduleInfo.scheduleInfo.toSchedule()
    startPlace = (
        addScheduleInfo.startPlace.toPlace()
        if addScheduleInfo.startPlace != None
        else None
    )
    endPlace = (
        addScheduleInfo.endPlace.toPlace() if addScheduleInfo.endPlace != None else None
    )

    scheduleCRUD.create(
        userEmail,
        schedule,
        startPlace,
        endPlace,
    )
