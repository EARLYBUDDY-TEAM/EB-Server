from eb_fast_api.service.notification.sources.schema.notification_transport import (
    BusRequestArrivalInfo,
    SubwayRequestArrivalInfo,
)
from eb_fast_api.service.realtime.sources import bus_realtime_service as bas
from eb_fast_api.service.realtime.sources.realtime_service_schema import ArrivalInfo
from typing import List


def get_bus_arrival_info(
    bus_real_time_info: BusRequestArrivalInfo,
) -> List[ArrivalInfo]:
    response = bas.get_bus_station_realtime_info(
        station_id=bus_real_time_info.station_id
    )
    if response.status_code != 200:
        return []

    try:
        arrival_info_list = bas.realtime_json_to_arrival_info(json=response.json())
    except Exception as e:
        return []

    return arrival_info_list
