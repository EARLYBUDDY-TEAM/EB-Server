from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.database.sources.crud import getDB
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo


router = APIRouter(prefix="/schedule")


@router.post("/add")
async def addSchedule(
    userEmail: str,
    scheduleInfo: ScheduleInfo,
    db=Depends(getDB),
):
    print(scheduleInfo)
    print("checkckckckckckkc")
    try:
        schedule_feature.createSchedule(
            userEmail,
            scheduleInfo,
            db,
        )
    except:
        # 다른 에러 상황은?
        raise HTTPException(
            status_code=400,
            detail="서버 스케줄 생성 에러",
        )

    db.commit()
    return
