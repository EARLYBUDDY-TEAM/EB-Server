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
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        return ScheduleCard(
            scheduleID=10,
            title="title",
            time=time,
            endPlaceName="endPlaceName",
        )


class ScheduleCardList(BaseModel):
    scheduleCardList: List[ScheduleCard]
