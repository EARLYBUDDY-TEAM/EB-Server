from httpx import AsyncClient, Response
from eb_fast_api.env.sources.env import ENV_API
from eb_fast_api.snippets.sources import dictionary, eb_datetime
from eb_fast_api.service.realtime.sources.error.subway_realtime_error import (
    GetSeoulSubwayRealtimeInfoError,
    FilterSubwayRealtimeDataError,
)
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from datetime import datetime
from typing import List


SubwayID = {
    "1001": "1호선",
    "1002": "2호선",
    "1003": "3호선",
    "1004": "4호선",
    "1005": "5호선",
    "1006": "6호선",
    "1007": "7호선",
    "1008": "8호선",
    "1009": "9호선",
    "1092": "우이신설경전철",
    "1067": "경춘선",
    "1063": "경의중앙선",
    "1075": "수인분당선",
    "1077": "신분당선",
    "1065": "공항철도",
}


def get_date_time_now() -> datetime:
    return eb_datetime.get_datetime_now()


async def get_seoul_subway_realtime_info(
    station_name: str,
) -> Response:
    apiKey = ENV_API.seoul_subway
    url = f"http://swopenAPI.seoul.go.kr/api/subway/{apiKey}/json/realtimeStationArrival/0/5/{station_name}"
    async with AsyncClient() as client:
        response = await client.get(url=url)
        return response


def filter_subway_realtime_data(
    data: dict,
    line_name: str,
    direction: int,
) -> RealTimeInfo:
    realtimeArrivalList = dictionary.safeDict(
        keyList=["realtimeArrivalList"], fromDict=data
    )
    realTimeInfo = RealTimeInfo(
        transport_number=line_name,
        arrival_sec1=None,
        left_station1=None,
        arrival_sec2=None,
        left_station2=None,
    )

    for realtimeData in realtimeArrivalList:
        subwayId = dictionary.safeDict(keyList=["subwayId"], fromDict=realtimeData)
        expectSubwayName = SubwayID[subwayId]
        if expectSubwayName != line_name:
            continue

        ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtimeData)
        if int(ordkey[0]) != direction:
            continue

        left_station = int(ordkey[2:5])

        arrival_sec: int = None
        data_create_time = dictionary.safeDict(
            keyList=["recptnDt"], fromDict=realtimeData
        )
        arrival_remain_time = dictionary.safeDict(
            keyList=["barvlDt"], fromDict=realtimeData
        )
        if (data_create_time != None) and (arrival_remain_time != None):
            data_create_time = datetime.strptime(data_create_time, "%Y-%m-%d %H:%M:%S")
            now = get_date_time_now()
            diff = now - data_create_time
            diff_total_seconds = int(diff.total_seconds())
            arrival_sec = diff_total_seconds + int(arrival_remain_time)

        if ordkey[1] == "1":
            realTimeInfo.left_station1 = left_station
            realTimeInfo.arrival_sec1 = arrival_sec
        elif ordkey[1] == "2":
            realTimeInfo.left_station2 = left_station
            realTimeInfo.arrival_sec2 = arrival_sec

    return realTimeInfo


async def request(
    station_name: str,
    line_name: str,
    direction: int,
) -> List[RealTimeInfo]:
    try:
        response_json = await get_seoul_subway_realtime_info(
            station_name=station_name,
        )
    except Exception as e:
        print(e)
        raise GetSeoulSubwayRealtimeInfoError()

    try:
        real_time_info = filter_subway_realtime_data(
            data=response_json,
            line_name=line_name,
            direction=direction,
        )
        return [real_time_info]
    except Exception as e:
        print(e)
        raise FilterSubwayRealtimeDataError()


"""
"02005성수0",
상하행코드(1자리),
순번(첫번째, 두번째 열차, 1자리),
첫번째 도착예정 정류장 - 현재 정류장(3자리),
목적지 정류장,
급행여부(1자리)

1. 역이름으로 호출
2. 호선으로 필터링
3. 상행 하행 필터링
leftstation - ordkey, arrivalsec - barvlDt

데이터 생성시간 + 남은시간 = 실제 열차의 도착시간
열차 도착시간 - 현재시간 = 실제 열차 도착까지의 남은시간

(0 : 상행/내선, 1 : 하행/외선)
"""
