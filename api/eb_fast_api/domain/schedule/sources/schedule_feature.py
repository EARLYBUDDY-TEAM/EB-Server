from fastapi import Depends
from sqlalchemy.orm import Session
from eb_fast_api.database.sources.database import get_db

from eb_fast_api.domain.schedule.sources.schedule_schema import ScheduleInfo
from eb_fast_api.database.sources.models import Schedule
from datetime import datetime


def create_schedule(scheduleInfo: ScheduleInfo):
    db: Session = Depends(get_db)
    schedule = Schedule(
        title=scheduleInfo.title,
        # time=datetime.fromisoformat(scheduleInfo.time),
        time=scheduleInfo.time,
        isNotify=scheduleInfo.isNotify,
        startPlace=None,
        endPlace=None,
    )
    db.add(schedule)
    db.commit()
