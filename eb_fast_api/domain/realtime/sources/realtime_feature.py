from httpx import AsyncClient, Response
from typing import List

from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfo
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


def real_time_json_to_real_time_info(json: dict) -> RealTimeInfo:
    transport_number: str = dictionary.safeDict(keyList=["routeNm"], fromDict=json)
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


def decode_real_time_info_list(
    json: dict,
) -> List[RealTimeInfo]:
    real_time_json_list = dictionary.safeDict(keyList=["result", "real"], fromDict=json)
    if real_time_json_list == None:
        raise Exception("real_time_json_list error")

    real_time_list = [
        real_time_json_to_real_time_info(json=real_time_json)
        for real_time_json in real_time_json_list
    ]

    real_time_list.sort(key=lambda x: x.arrival_sec1 or float("inf"))

    return real_time_list
