from pydantic import BaseModel
from typing import List
from eb_fast_api.domain.schema.sources.schema import ScheduleInfo
from eb_fast_api.database.sources.model.models import Schedule


class ScheduleSchemaList(BaseModel):
    datas: List[ScheduleInfo]


class ScheduleSchema(ScheduleInfo):
    scheduleID: int

    def __init__(self, schedule: Schedule):
        scheduleDict = schedule.__dict__

        super().__init__(
            title=scheduleDict["title"],
            memo=scheduleDict["memo"],
            time=scheduleDict["time"],
            isNotify=scheduleDict["isNotify"],
            startPlaceID=scheduleDict["startPlaceID"],
            endPlaceID=scheduleDict["endPlaceID"],
            scheduleID=scheduleDict["id"],
        )
