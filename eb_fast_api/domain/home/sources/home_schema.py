from pydantic import BaseModel
from typing import List, Self
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo


class ScheduleSchemaList(BaseModel):
    scheduleSchemaList: List[ScheduleInfo]


class ScheduleSchema(ScheduleInfo):
    scheduleID: int

    @classmethod
    def mock(cls) -> Self:
        scheduleInfo = ScheduleInfo.mock()
        return ScheduleSchema(
            scheduleID=10,
            title=scheduleInfo.title,
            memo=scheduleInfo.memo,
            time=scheduleInfo.time,
            isNotify=scheduleInfo.isNotify,
            startPlaceInfo=scheduleInfo.startPlaceInfo,
            endPlaceInfo=scheduleInfo.endPlaceInfo,
        )
