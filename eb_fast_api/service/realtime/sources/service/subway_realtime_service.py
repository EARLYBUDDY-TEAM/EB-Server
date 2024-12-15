from httpx import AsyncClient, Response
from eb_fast_api.env.sources.env import ENV_API
from eb_fast_api.snippets.sources import dictionary, eb_datetime
from eb_fast_api.service.realtime.sources.realtime_service_schema import (
    RealTimeInfo,
    ArrivalInfo,
)
from datetime import datetime
from typing import List, Optional


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


def is_same_line_name(
    line_name: str,
    realtime_json: dict,
) -> bool:
    subwayId = dictionary.safeDict(keyList=["subwayId"], fromDict=realtime_json)
    expectSubwayName = SubwayID[subwayId]
    return expectSubwayName == line_name


def is_same_direction(
    direction: int,
    ordkey: str,
) -> bool:
    try:
        expect_direction = int(ordkey[0])
        return expect_direction == direction
    except Exception as e:
        print(e)
        return False


def cal_arrival_sec(realtime_json: dict) -> Optional[int]:
    arrival_sec = None
    data_create_time = dictionary.safeDict(
        keyList=["recptnDt"],
        fromDict=realtime_json,
    )
    arrival_remain_time = dictionary.safeDict(
        keyList=["barvlDt"],
        fromDict=realtime_json,
    )

    if (data_create_time != None) and (arrival_remain_time != None):
        data_create_time = datetime.strptime(data_create_time, "%Y-%m-%d %H:%M:%S")
        now = get_date_time_now()
        diff = now - data_create_time
        diff_total_seconds = int(diff.total_seconds())
        arrival_sec = diff_total_seconds + int(arrival_remain_time)
        # 남은 시간 + abs(데이터 생성 시간 - 현재 시간)

    return arrival_sec


def filter_subway_realtime_data(
    data: dict,
    line_name: str,
    direction: int,
) -> RealTimeInfo:
    realtimeArrivalList = dictionary.safeDict(
        keyList=["realtimeArrivalList"], fromDict=data
    )

    realtime_info = RealTimeInfo(
        transport_number=line_name,
        arrival_info1=ArrivalInfo(
            transport_plate=None,
            arrival_sec=None,
            left_station=None,
        ),
        arrival_info2=ArrivalInfo(
            transport_plate=None,
            arrival_sec=None,
            left_station=None,
        ),
    )

    for realtime_json in realtimeArrivalList:
        if not is_same_line_name(
            line_name=line_name,
            realtime_json=realtime_json,
        ):
            continue

        ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtime_json)
        if ordkey is None:
            continue

        if not is_same_direction(
            direction=direction,
            ordkey=ordkey,
        ):
            continue

        try:
            left_station = int(ordkey[2:5])
            arrival_sec = cal_arrival_sec(realtime_json=realtime_json)
            transport_plate = dictionary.safeDict(
                keyList=["btrainNo"], fromDict=realtime_json
            )
            if ordkey[1] == "1":
                realtime_info.arrival_info1.left_station = left_station
                realtime_info.arrival_info1.arrival_sec = arrival_sec
                realtime_info.arrival_info1.transport_plate = transport_plate
            elif ordkey[1] == "2":
                realtime_info.arrival_info2.left_station = left_station
                realtime_info.arrival_info2.arrival_sec = arrival_sec
                realtime_info.arrival_info2.transport_plate = transport_plate
        except Exception as e:
            print(e)
            continue

    return realtime_info


async def request(
    station_name: str,
    line_name: str,
    direction: int,
) -> List[RealTimeInfo]:
    try:
        response = await get_seoul_subway_realtime_info(
            station_name=station_name,
        )
        response_json = response.json()
    except Exception as e:
        print(e)
        raise Exception("get_seoul_subway_realtime_info_error")

    real_time_info = filter_subway_realtime_data(
        data=response_json,
        line_name=line_name,
        direction=direction,
    )
    return [real_time_info]


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
