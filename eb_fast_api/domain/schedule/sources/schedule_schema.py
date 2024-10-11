from pydantic import BaseModel
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo, PlaceInfo
from typing import Optional


class AddScheduleInfo(BaseModel):
    scheduleInfo: ScheduleInfo
    startPlace: Optional[PlaceInfo]
    endPlace: Optional[PlaceInfo]

    @classmethod
    def mock(cls):
        scheduleInfo = ScheduleInfo.mock()
        startPlace = PlaceInfo.mock()
        endPlace = PlaceInfo.mock()
        startPlace.id = scheduleInfo.startPlaceID
        endPlace.id = scheduleInfo.endPlaceID

        return AddScheduleInfo(
            scheduleInfo=scheduleInfo,
            startPlace=startPlace,
            endPlace=endPlace,
        )
