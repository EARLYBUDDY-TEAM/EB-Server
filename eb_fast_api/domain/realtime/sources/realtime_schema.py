from pydantic import BaseModel
from typing import List
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo


class RealTimeInfoList(BaseModel):
    real_time_info_list: List[RealTimeInfo]
