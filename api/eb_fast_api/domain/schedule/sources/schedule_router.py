from fastapi import APIRouter

from eb_fast_api.domain.schedule.sources.schedule_schema import ScheduleInfo
from eb_fast_api.domain.schedule.sources import schedule_feature

router = APIRouter(prefix='/schedule')

@router.post('/add')
async def add_schedule(scheduleInfo: ScheduleInfo):
    schedule_feature.create_schedule(scheduleInfo)
    return