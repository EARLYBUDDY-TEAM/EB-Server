from pydantic import BaseModel
from datetime import datetime


class ScheduleCard(BaseModel):
    scheduleID: int
    title: str
    time: datetime
    endPlaceName: str
