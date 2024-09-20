from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/schedule")


@router.post("/add")
async def addSchedule(
    scheduleInfo: ScheduleInfo,
    userEmail: str,
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
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
