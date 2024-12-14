from pydantic import BaseModel
from typing import Optional, Self


class RealTimeInfo(BaseModel):
    transport_number: str
    arrival_sec1: Optional[int]
    left_station1: Optional[int]
    arrival_sec2: Optional[int]
    left_station2: Optional[int]

    @classmethod
    def mock(cls) -> Self:
        return RealTimeInfo(
            transport_number="transport_number",
            arrival_sec1=1,
            left_station1=1,
            arrival_sec2=1,
            left_station2=1,
        )
