from fastapi import Depends
from eb_fast_api.domain.schedule.sources.schedule_schema import ScheduleInfo
from eb_fast_api.database.sources.models import Schedule, Place
from eb_fast_api.database.sources.crud import getDB


def create_schedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    db=Depends(getDB), # router에서 주입하기
):
    schedule = Schedule(
        title=scheduleInfo.title,
        memo=scheduleInfo.memo,
        time=scheduleInfo.time,
        isNotify=scheduleInfo.isNotify,
    )

    if scheduleInfo.startPlace is not None:
        p = scheduleInfo.startPlace
        schedule.startPlaceID = p.id
        startPlace = Place(
            id=p.id,
            name=p.name,
            address=p.address,
            category=p.category,
            distance=p.distance,
            coordiX=p.coordi.x,
            coordiY=p.coordi.y,
        )
        db.placeCreate(startPlace)

    if scheduleInfo.endPlace is not None:
        p = scheduleInfo.endPlace
        schedule.endPlaceID = p.id
        endPlace = Place(
            id=p.id,
            name=p.name,
            address=p.address,
            category=p.category,
            distance=p.distance,
            coordiX=p.coordi.x,
            coordiY=p.coordi.y,
        )
        db.placeCreate(endPlace)

    db.scheduleCreate(
        userEmail,
        schedule,
        startPlace,
        endPlace,
    )

    db.commit()
