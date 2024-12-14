from eb_fast_api.service.notification.sources.schema.notification_transport import (
    BusRequestRealTimeInfo,
    SubwayRequestRealTimeInfo,
    NotificationTransport,
    RequestRealTimeInfo,
    ArrivalInfo,
)
from eb_fast_api.service.realtime.sources.service import bus_realtime_service as brs
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from typing import List
from typing import Optional
from eb_fast_api.snippets.sources import dictionary


###
def is_transport_duplicate(
    realtime_info: RealTimeInfo,
    request_real_time_info: RequestRealTimeInfo,
) -> bool:
    dup = request_real_time_info.dup
    transport_number = realtime_info.transport_number
    transport_plate = realtime_info.transport_plate
    cached_transport_plate = dictionary.safeDict(
        keyList=[transport_number],
        fromDict=dup,
    )

    if cached_transport_plate == transport_plate:
        return True
    else:
        dup[transport_number] = transport_plate
        return False


###
def get_arrival_info(
    real_time_info_list: List[RealTimeInfo],
    request_real_time_info: RequestRealTimeInfo,
    arrival_before: int,
) -> Optional[ArrivalInfo]:
    for real_time_info in real_time_info_list:
        arrival_minute = real_time_info.arrival_sec1 / 60

        if arrival_before < arrival_minute:
            continue

        if is_transport_duplicate(
            realtime_info=real_time_info,
            request_real_time_info=request_real_time_info,
        ):
            continue

        transport_number = real_time_info.transport_number
        return ArrivalInfo(
            transport_number=transport_number,
            arrival_minute=arrival_minute,
        )
    else:
        return None
