from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/schedule")


@router.post("/add")
async def addSchedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    scheduleCRUD=Depends(EBDataBase.schedule.createCRUD),
):
    try:
        schedule_feature.createSchedule(
            userEmail,
            scheduleInfo,
            scheduleCRUD,
        )
    except:
        # 다른 에러 상황은?
        raise HTTPException(
            status_code=400,
            detail="서버 스케줄 생성 에러",
        )

    scheduleCRUD.commit()
    return
