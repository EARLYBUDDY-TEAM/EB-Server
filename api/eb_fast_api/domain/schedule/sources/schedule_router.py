from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.domain.schema.schedule_info import ScheduleInfo


router = APIRouter(prefix="/schedule")


@router.post("/add")
async def add_schedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    db=Depends(getDB),
):
    try:
        schedule_feature.createSchedule(
            userEmail,
            scheduleInfo,
            db,
        )
    except:
        raise HTTPException(
            status_code=500,
            detail="서버 스케줄 생성 에러",
        )

    db.commit()
    return
