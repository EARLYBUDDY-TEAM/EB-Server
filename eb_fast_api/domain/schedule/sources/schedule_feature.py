from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD, PlaceCRUD


def createSchedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
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

    if startPlace is not None or endPlace is not None:
        placeCRUD = PlaceCRUD(session=scheduleCRUD.session)
        if startPlace is not None:
            placeCRUD.create(startPlace)
        if endPlace is not None:
            placeCRUD.create(endPlace)

    schedule = scheduleInfo.toSchedule()

    scheduleCRUD.create(
        userEmail=userEmail,
        schedule=schedule,
    )

    scheduleCRUD.commit()


def update_schedule_with_info(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD: ScheduleCRUD,
):
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

    if startPlace is not None or endPlace is not None:
        placeCRUD = PlaceCRUD(session=scheduleCRUD.session)
        if startPlace is not None:
            placeCRUD.create(startPlace)
        if endPlace is not None:
            placeCRUD.create(endPlace)

    to_update_schedule = scheduleInfo.toSchedule()

    scheduleCRUD.update(
        userEmail=userEmail,
        to_update_schedule=to_update_schedule,
    )
