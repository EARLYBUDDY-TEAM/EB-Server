from pydantic import BaseModel
from typing import Optional, Self
from datetime import datetime
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.domain.schema.sources.place_info import PlaceInfo
from uuid import uuid4


class ScheduleInfo(BaseModel):
    id: Optional[str]
    title: str
    memo: Optional[str]
    time: datetime
    notify_schedule: Optional[int]
    notify_transport: Optional[int]
    notify_transport_range: Optional[int]
    startPlaceInfo: Optional[PlaceInfo]
    endPlaceInfo: Optional[PlaceInfo]

    def toSchedule(self, id: Optional[str] = None) -> Schedule:
        startPlaceID = self.startPlaceInfo.id if self.startPlaceInfo != None else None
        endPlaceID = self.endPlaceInfo.id if self.endPlaceInfo != None else None
        schedule_id = self.id
        if schedule_id == None:
            schedule_id = id
            if schedule_id == None:
                schedule_id = str(uuid4())

        schedule = Schedule(
            id=schedule_id,
            title=self.title,
            memo=self.memo,
            time=self.time,
            notify_schedule=self.notify_schedule,
            notify_transport=self.notify_transport,
            notify_transport_range=self.notify_transport_range,
            startPlaceID=startPlaceID,
            endPlaceID=endPlaceID,
        )
        return schedule
    

    @classmethod
    def mock(
        cls,
        id: Optional[str] = None,
    ) -> Self:
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        time = time.replace(microsecond=0, tzinfo=None)
        startPlaceInfo = PlaceInfo.mock()
        startPlaceInfo.id = "startPlaceID"
        endPlaceInfo = PlaceInfo.mock()
        endPlaceInfo.id = "endPlaceID"

        return ScheduleInfo(
            id=id or str(uuid4()),
            title="title",
            memo="memo",
            time=time,
            notify_schedule=10,
            notify_transport=10,
            notify_transport_range=10,
            startPlaceInfo=startPlaceInfo,
            endPlaceInfo=endPlaceInfo,
        )
