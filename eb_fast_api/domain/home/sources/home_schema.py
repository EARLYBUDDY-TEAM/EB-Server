from pydantic import BaseModel
from typing import List
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo


class ScheduleInfoList(BaseModel):
    all_schedules: List[ScheduleInfo]
