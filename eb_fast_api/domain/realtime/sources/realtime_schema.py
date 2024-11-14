from pydantic import BaseModel
from typing import List, Optional, Self
from eb_fast_api.snippets.sources import dictionary


class RealTimeInfo(BaseModel):
    transport_number: str
    arrival_sec1: Optional[int]
    left_station1: Optional[int]
    arrival_sec2: Optional[int]
    left_station2: Optional[int]


class RealTimeInfoList(BaseModel):
    real_time_info_list: List[RealTimeInfo]


class SubwaySchedule(BaseModel):
    departure_time: str
    first_last_flag: int

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        departure_time: str = dictionary.safeDict(keyList=["departureTime"], fromDict=j)
        first_last_flag: int = dictionary.safeDict(
            keyList=["firstLastFlag"], fromDict=j
        )

        return SubwaySchedule(
            departure_time=departure_time,
            first_last_flag=first_last_flag,
        )


class TotalSubwaySchedule(BaseModel):
    weekday_schedule: List[SubwaySchedule]
    saturday_schedule: List[SubwaySchedule]
    holiday_schedule: List[SubwaySchedule]
