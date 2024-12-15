from httpx import AsyncClient, Response
from typing import List, Optional
from eb_fast_api.service.realtime.sources.realtime_service_schema import (
    RealTimeInfo,
    ArrivalInfo,
)
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


def arrival_json_to_arrival_info(
    json: Optional[dict],
) -> ArrivalInfo:
    arrival_sec1 = dictionary.safeDict(keyList=["arrivalSec"], fromDict=json)
    left_station1 = dictionary.safeDict(keyList=["leftStation"], fromDict=json)
    transport_plate = dictionary.safeDict(keyList=["busPlateNo"], fromDict=json)

    return ArrivalInfo(
        arrival_sec=arrival_sec1,
        left_station=left_station1,
        transport_plate=transport_plate,
    )


def realtime_json_to_realtime_info(json: dict) -> Optional[RealTimeInfo]:
    transport_number = dictionary.safeDict(
        keyList=["routeNm"],
        fromDict=json,
    )
    if transport_number == None:
        return None

    arrival1_dict = dictionary.safeDict(
        keyList=["arrival1"],
        fromDict=json,
    )
    arrival_info1 = arrival_json_to_arrival_info(json=arrival1_dict)

    arrival2_dict = dictionary.safeDict(
        keyList=["arrival2"],
        fromDict=json,
    )
    arrival_info2 = arrival_json_to_arrival_info(json=arrival2_dict)

    return RealTimeInfo(
        transport_number=transport_number,
        arrival_info1=arrival_info1,
        arrival_info2=arrival_info2,
    )


def decode_realtime_info_list(
    json: dict,
) -> List[RealTimeInfo]:
    arrival_info_json_list = dictionary.safeDict(
        keyList=["result", "real"], fromDict=json
    )
    if arrival_info_json_list == None:
        return []

    realtime_info_list = []
    for arrival_info_json in arrival_info_json_list:
        realtime_info = realtime_json_to_realtime_info(
            json=arrival_info_json,
        )
        if realtime_info is None:
            continue
        realtime_info_list.append(realtime_info)

    realtime_info_list.sort(key=lambda x: x.arrival_info1.arrival_sec or float("inf"))

    return realtime_info_list


async def request(
    station_id: int,
) -> List[RealTimeInfo]:
    try:
        response = await get_bus_station_realtime_info(
            station_id=station_id,
        )
        response_json = response.json()
    except Exception as e:
        print(e)
        raise Exception("GetBusStationRealtimeJsonError")

    real_time_info_list = decode_realtime_info_list(json=response_json)
    return real_time_info_list
