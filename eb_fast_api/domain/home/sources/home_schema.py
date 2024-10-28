from pydantic import BaseModel
from typing import Optional, Self, List
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from uuid import uuid4


class SchedulePathInfo(BaseModel):
    schedule_info: ScheduleInfo
    path_info: Optional[PathInfo]

    @classmethod
    def mock(cls, id: str = str(uuid4())) -> Self:
        return SchedulePathInfo(
            schedule_info=ScheduleInfo.mock(id=id),
            path_info=PathInfo.mock(),
        )


class SchedulePathInfoList(BaseModel):
    all_schedules: List[SchedulePathInfo]