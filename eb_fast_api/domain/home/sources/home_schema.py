from pydantic import BaseModel
from datetime import datetime
from typing import List, Self


class ScheduleCard(BaseModel):
    scheduleID: int
    title: str
    time: datetime
    endPlaceName: str

    @classmethod
    def mock(cls) -> Self:
        return ScheduleCard(
            scheduleID=10,
            title="title",
            time=datetime.now(),
            endPlaceName="endPlaceName",
        )


class ScheduleCardList(BaseModel):
    scheduleCardList: List[ScheduleCard]
