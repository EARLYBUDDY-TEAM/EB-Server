from eb_fast_api.service.notification.sources.schema.notification_transport import (
    BusRequestRealTimeInfo,
    SubwayRequestRealTimeInfo,
    NotificationTransport,
)
from eb_fast_api.service.realtime.sources.service import bus_realtime_service as brs
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from typing import List
from typing import Optional
from eb_fast_api.snippets.sources import dictionary


"""
# title
# {스케줄 이름, schedule_name}


# body
# {버스 or 지하철, transport_type} {202번} {역 or 정류장, station_name} 도착까지 {30, noti_arrival_before}분 남았습니다.

{버스 or 지하철} {202번} {역 or 정류장} 도착까지 {30}분 남았습니다.
알림 범위 : 120분
도착전 : 60분

realtime_info transport number 추가
"""


def is_bus_duplicate(
    realtime_info: RealTimeInfo,
    bus_request_real_time_info: BusRequestRealTimeInfo,
) -> bool:
    dup = bus_request_real_time_info.dup
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


def get_bus_arrival_info(
    real_time_info_list: List[RealTimeInfo],
    bus_request_real_time_info: BusRequestRealTimeInfo,
    arrival_before: int,
) -> Optional[tuple]:
    for real_time_info in real_time_info_list:
        arrival_minute = real_time_info.arrival_sec1 / 60

        if arrival_before < arrival_minute:
            continue

        if is_bus_duplicate(
            realtime_info=real_time_info,
            bus_request_real_time_info=bus_request_real_time_info,
        ):
            continue

        transport_number = real_time_info.transport_number
        return (transport_number, arrival_minute)
    else:
        return None


async def make_bus_notification_body(
    bus_request_real_time_info: BusRequestRealTimeInfo,
    arrival_before: int,
    station_name: str,
) -> Optional[str]:
    station_id = bus_request_real_time_info.station_id
    real_time_info_list = await brs.request(station_id=station_id)

    bus_arrival_info = get_bus_arrival_info(
        real_time_info_list=real_time_info_list,
        bus_request_real_time_info=bus_request_real_time_info,
        arrival_before=arrival_before,
    )

    if bus_arrival_info == None:
        return None

    transport_type = "버스"
    transport_number, arrival_minute = bus_arrival_info

    return f"{transport_type} {transport_number}번 {station_name} 도착까지 {arrival_minute}분 남았습니다."


async def make_body(
    noti_transport: NotificationTransport,
) -> Optional[str]:
    request_real_time_info = noti_transport.request_real_time_info
    if isinstance(request_real_time_info, BusRequestRealTimeInfo):
        return await make_bus_notification_body(
            bus_request_real_time_info=request_real_time_info,
            arrival_before=noti_transport.noti_content.arrival_before,
            station_name=noti_transport.noti_content.station_name,
        )
    elif isinstance(request_real_time_info, SubwayRequestRealTimeInfo):
        return await make_subway_notification_body(
            subway_request_real_time_info=request_real_time_info,
            arrival_before=noti_transport.noti_content.arrival_before,
            station_name=noti_transport.noti_content.station_name,
        )
    else:
        return None


async def make_subway_notification_body(
    subway_request_real_time_info: SubwayRequestRealTimeInfo,
    arrival_before: int,
    station_name: str,
) -> Optional[str]:
    return None
