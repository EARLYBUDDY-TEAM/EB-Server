from fastapi import APIRouter, Depends, HTTPException
from typing import List
from eb_fast_api.domain.home.sources import home_feature
from eb_fast_api.domain.home.sources.home_schema import (
    ScheduleSchemaList,
    ScheduleSchema,
)
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/home")


@router.get("/get_all_schedules")
def get_all_schedules(
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
) -> ScheduleSchemaList:
    scheduleList = home_feature.read_all_schedule(
        userEmail=userEmail,
        scheduleCRUD=scheduleCRUD,
    )

    datas: List[ScheduleSchema] = [
        ScheduleSchema(schedule=schedule) for schedule in scheduleList
    ]

    scheduleSchemaList = ScheduleSchemaList(datas=datas)
    return scheduleSchemaList


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
