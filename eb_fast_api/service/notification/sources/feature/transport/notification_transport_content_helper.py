from eb_fast_api.service.notification.sources.schema.notification_transport import (
    RequestRealTimeInfo,
)
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from typing import List
from typing import Optional
from eb_fast_api.snippets.sources import dictionary
from eb_fast_api.snippets.sources.logger import logger


def is_transport_duplicate(
    realtime_info: RealTimeInfo,
    request_real_time_info: RequestRealTimeInfo,
) -> bool:
    dup = request_real_time_info.dup
    transport_number = realtime_info.transport_number
    transport_plate = realtime_info.arrival_info1.transport_plate
    cached_transport_plate = dictionary.safeDict(
        keyList=[transport_number],
        fromDict=dup,
    )

    if cached_transport_plate == transport_plate:
        return True
    else:
        dup[transport_number] = transport_plate
        return False


def get_arrival_info(
    realtime_info_list: List[RealTimeInfo],
    request_real_time_info: RequestRealTimeInfo,
    arrival_before: int,
) -> Optional[tuple]:
    for realtime_info in realtime_info_list:
        arrival_sec = realtime_info.arrival_info1.arrival_sec
        if arrival_sec is None:
            continue

        arrival_minute = arrival_sec // 60

        if arrival_before < arrival_minute:
            continue

        if is_transport_duplicate(
            realtime_info=realtime_info,
            request_real_time_info=request_real_time_info,
        ):
            continue

        transport_number = realtime_info.transport_number
        return (transport_number, arrival_minute)
    else:
        return None
