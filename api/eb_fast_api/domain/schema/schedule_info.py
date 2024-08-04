from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from eb_fast_api.database.sources.model import Schedule
from eb_fast_api.domain.schema.place_info import PlaceInfo


class ScheduleInfo(BaseModel):
    title: str
    time: datetime
    isNotify: bool
    memo: Optional[str] = None
    startPlace: Optional[PlaceInfo] = None
    endPlace: Optional[PlaceInfo] = None

    def toSchedule(self) -> Schedule:
        schedule = Schedule(
            title = self.title,
            time = self.time,
            isNotify = self.isNotify,
            memo = self.memo,
        )

        if self.startPlace != None:
            schedule.startPlaceID = self.startPlace.id
        
        if self.endPlace != None:
            schedule.endPlaceID = self.endPlace.id
        
        return schedule

    @classmethod
    def mock(cls):
        return ScheduleInfo(
            title = 'title',
            memo = 'memo',
            time = datetime.now(),
            isNotify = False,
            startPlace = None,
            endPlace = None,
        )
