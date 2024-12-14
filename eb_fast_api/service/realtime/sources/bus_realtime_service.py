from httpx import AsyncClient, Response
from typing import List, Optional
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from eb_fast_api.env.sources.env import ENV_API
from eb_fast_api.snippets.sources import dictionary


async def get_bus_station_realtime_info(
    station_id: int,
) -> Response:
    url = "https://api.odsay.com/v1/api/realtimeStation"
    params = {
        "apiKey": ENV_API.odsay,
        "stationID": station_id,
        "stationBase": 0,
    }
    async with AsyncClient() as client:
        response = await client.get(url=url, params=params)
        return response


def realtime_json_to_realtime_info(json: dict) -> RealTimeInfo:
    transport_number: Optional[str] = dictionary.safeDict(
        keyList=["routeNm"], fromDict=json
    )
    arrival_sec1 = dictionary.safeDict(
        keyList=["arrival1", "arrivalSec"], fromDict=json
    )
    left_station1 = dictionary.safeDict(
        keyList=["arrival1", "leftStation"], fromDict=json
    )
    arrival_sec2 = dictionary.safeDict(
        keyList=["arrival2", "arrivalSec"], fromDict=json
    )
    left_station2 = dictionary.safeDict(
        keyList=["arrival2", "leftStation"], fromDict=json
    )

    if transport_number == None:
        raise Exception("decode transport_number error")

    return RealTimeInfo(
        transport_number=transport_number,
        arrival_sec1=arrival_sec1,
        left_station1=left_station1,
        arrival_sec2=arrival_sec2,
        left_station2=left_station2,
    )


def decode_realtime_info_list(
    json: dict,
) -> List[RealTimeInfo]:
    arrival_info_json_list = dictionary.safeDict(
        keyList=["result", "real"], fromDict=json
    )
    if arrival_info_json_list == None:
        raise Exception("arrival_info_json_list error")

    arrival_info_list = [
        realtime_json_to_realtime_info(json=arrival_info_json)
        for arrival_info_json in arrival_info_json_list
    ]

    arrival_info_list.sort(key=lambda x: x.arrival_sec1 or float("inf"))

    return arrival_info_list
