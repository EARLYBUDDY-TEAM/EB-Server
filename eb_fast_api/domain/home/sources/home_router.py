from fastapi import APIRouter, Depends, HTTPException
from typing import List
from eb_fast_api.domain.home.sources import home_feature
from eb_fast_api.domain.home.sources.home_schema import ScheduleInfoList
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/home")


@router.get("/get_all_schedules")
def get_all_schedules(
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
    placeCRUD=Depends(EBDataBase.place.getCRUD),
) -> ScheduleInfoList:
    scheduleList = home_feature.read_all_schedule(
        userEmail=userEmail,
        scheduleCRUD=scheduleCRUD,
    )

    all_schedules: List[ScheduleInfo] = [
        home_feature.schedule_to_schedule_info(
            schedule=schedule,
            placeCRUD=placeCRUD,
        )
        for schedule in scheduleList
    ]

    scheduleInfoList = ScheduleInfoList(all_schedules=all_schedules)
    return scheduleInfoList


@router.delete("/delete_schedule")
def delete_schedule(
    scheduleID: int,
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
):
    try:
        scheduleCRUD.delete(
            userEmail=userEmail,
            scheduleID=scheduleID,
        )
        scheduleCRUD.commit()
    except:
        raise HTTPException(
            status_code=400,
            detail="스케줄 삭제 에러",
        )
