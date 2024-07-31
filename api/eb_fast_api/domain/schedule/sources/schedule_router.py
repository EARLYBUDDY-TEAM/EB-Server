from fastapi import APIRouter, HTTPException

from eb_fast_api.domain.schedule.sources.schedule_schema import ScheduleInfo
from eb_fast_api.domain.schedule.sources import schedule_feature

router = APIRouter(prefix='/schedule')

@router.post('/add')
async def add_schedule(userEmail: str, scheduleInfo: ScheduleInfo):
    try:
        schedule_feature.create_schedule(userEmail, scheduleInfo)
    except:
        raise HTTPException(
            status_code = 500,
            detail = "서버 스케줄 생성 에러",
        )
    return