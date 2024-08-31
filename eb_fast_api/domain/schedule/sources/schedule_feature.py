from eb_fast_api.domain.schema.sources.schema import ScheduleInfo


def createSchedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    db,
):
    schedule = scheduleInfo.toSchedule()
    startPlace = (
        scheduleInfo.startPlace.toPlace() if scheduleInfo.startPlace != None else None
    )
    endPlace = (
        scheduleInfo.endPlace.toPlace() if scheduleInfo.endPlace != None else None
    )

    db.scheduleCreate(
        userEmail,
        schedule,
        startPlace,
        endPlace,
    )
