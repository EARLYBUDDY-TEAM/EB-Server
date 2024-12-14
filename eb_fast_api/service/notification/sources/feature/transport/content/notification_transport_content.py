from eb_fast_api.service.notification.sources.schema.notification_transport import (
    BusRequestRealTimeInfo,
    SubwayRequestRealTimeInfo,
    NotificationTransport,
)
from eb_fast_api.service.realtime.sources.service import bus_realtime_service as brs
from eb_fast_api.service.realtime.sources.service import subway_realtime_service as srs
from eb_fast_api.service.notification.sources.feature.transport.content.notification_transport_content_helper import (
    get_arrival_info,
)
from typing import Optional


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


async def make_subway_notification_body(
    subway_request_real_time_info: SubwayRequestRealTimeInfo,
    station_name: str,
    arrival_before: int,
) -> Optional[str]:
    line_name = subway_request_real_time_info.line_name
    direction = subway_request_real_time_info.direction

    real_time_info_list = await srs.request(
        station_name=station_name,
        line_name=line_name,
        direction=direction,
    )

    subway_arrival_info = get_arrival_info(
        real_time_info_list=real_time_info_list,
        request_real_time_info=subway_request_real_time_info,
        arrival_before=arrival_before,
    )

    if subway_arrival_info == None:
        return None

    transport_type = "지하철"
    transport_number = subway_arrival_info.transport_number
    arrival_minute = subway_arrival_info.arrival_minute

    return f"{transport_type} {transport_number} {station_name} 도착까지 {arrival_minute}분 남았습니다."


async def make_bus_notification_body(
    bus_request_real_time_info: BusRequestRealTimeInfo,
    arrival_before: int,
    station_name: str,
) -> Optional[str]:
    station_id = bus_request_real_time_info.station_id
    real_time_info_list = await brs.request(station_id=station_id)

    bus_arrival_info = get_arrival_info(
        real_time_info_list=real_time_info_list,
        request_real_time_info=bus_request_real_time_info,
        arrival_before=arrival_before,
    )

    if bus_arrival_info == None:
        return None

    transport_type = "버스"
    transport_number = bus_arrival_info.transport_number
    arrival_minute = bus_arrival_info.arrival_minute

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
