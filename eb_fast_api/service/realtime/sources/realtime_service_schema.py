from pydantic import BaseModel
from typing import Optional, Self


class ArrivalInfo(BaseModel):
    transport_plate: Optional[str]
    arrival_sec: Optional[int]
    left_station: Optional[int]

    @classmethod
    def mock(cls) -> Self:
        return ArrivalInfo(
            transport_plate="transport_plate",
            arrival_sec=120,
            left_station=1,
        )


class RealTimeInfo(BaseModel):
    transport_number: str
    arrival_info1: ArrivalInfo
    arrival_info2: ArrivalInfo

    @classmethod
    def mock(cls) -> Self:
        return RealTimeInfo(
            transport_number="transport_number",
            arrival_info1=ArrivalInfo.mock(),
            arrival_info2=ArrivalInfo.mock(),
        )
