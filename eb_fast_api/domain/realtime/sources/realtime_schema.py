from pydantic import BaseModel
from typing import List, Optional


class RealTimeInfo(BaseModel):
    transport_number: str
    arrival_sec1: Optional[int]
    arrival_sec2: Optional[int]


class RealTimeInfoList(BaseModel):
    real_time_info_list: List[RealTimeInfo]
