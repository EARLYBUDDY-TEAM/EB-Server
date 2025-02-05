from eb_fast_api.snippets.sources import dictionary, eb_datetime
from datetime import datetime
from typing import List


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
    # "1092": "우이신설경전철",
    "1092": "우이신설선",
    "1067": "경춘선",
    "1063": "경의중앙선",
    "1075": "수인분당선",
    "1077": "신분당선",
    "1065": "공항철도",
    "1032": "GTX-A",
}


def get_date_time_now() -> datetime:
    return eb_datetime.get_datetime_now()


def is_same_line_name(
    line_name: str,
    realtime_json: dict,
) -> bool:
    try:
        subwayId = dictionary.safeDict(keyList=["subwayId"], fromDict=realtime_json)
        expectSubwayName = dictionary.safeDict(keyList=[subwayId], fromDict=SubwayID)
        if expectSubwayName == line_name:
            return True
        else:
            return False
    except:
        return False


def is_same_direction(
    up_or_down: int,
    realtime_json: dict,
) -> bool:
    try:
        ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtime_json)
        if not ordkey:
            return False

        expect_up_or_down = int(ordkey[0])
        if expect_up_or_down == up_or_down:
            return True
        else:
            return False
    except Exception as e:
        return False


def is_left_station_not_zero(
    realtime_json: dict,
) -> bool:
    try:
        left_station = int(realtime_json["ordkey"][2:5])
        return left_station != 0
    except Exception as e:
        return False


def lambda_realtime_arrival_list_sort(
    realtime_json: dict,
) -> int:
    try:
        left_station = int(realtime_json["ordkey"][2:5])
        return left_station
    except Exception as e:
        return float("inf")


def lambda_realtime_arrival_list_filter(
    up_or_down: int,
    line_name: str,
    realtime_json: dict,
) -> bool:
    try:
        is_same_direction_result = is_same_direction(
            up_or_down=up_or_down,
            realtime_json=realtime_json,
        )
        is_same_line_name_result = is_same_line_name(
            line_name=line_name,
            realtime_json=realtime_json,
        )
        is_left_station_not_zero_result = is_left_station_not_zero(
            realtime_json=realtime_json,
        )

        if (
            is_same_direction_result
            and is_same_line_name_result
            and is_left_station_not_zero_result
        ):
            return True
        else:
            return False
    except Exception as e:
        return False


def filter_dup_realtime_arrival_list(
    realtime_arrival_list: List[dict],
) -> List[dict]:
    def lambda_realtime_arrival_list_sort(
        realtime_arrival: dict,
    ) -> datetime:
        data_create_time = dictionary.safeDict(
            keyList=["recptnDt"],
            fromDict=realtime_arrival,
        )
        if data_create_time is None:
            return datetime.min
        data_create_time = datetime.strptime(data_create_time, "%Y-%m-%d %H:%M:%S")
        return data_create_time

    sorted_realtime_arrival_list = sorted(
        realtime_arrival_list,
        key=lambda realtime_arrival: lambda_realtime_arrival_list_sort(
            realtime_arrival
        ),
        reverse=True,
    )

    tmp_filtered_dict = dict()
    for realtime_arrival in sorted_realtime_arrival_list:
        transport_plate = dictionary.safeDict(
            keyList=["btrainNo"],
            fromDict=realtime_arrival,
        )
        if transport_plate is None:
            continue
        if transport_plate in tmp_filtered_dict:
            continue
        tmp_filtered_dict[transport_plate] = realtime_arrival

    return list(tmp_filtered_dict.values())


def filter_subway_realtime_json(
    json: dict,
    line_name: str,
    up_or_down: int,
) -> List[dict]:
    realtimeArrivalList = dictionary.safeDict(
        keyList=["realtimeArrivalList"], fromDict=json
    )

    # 가장 최신 데이터(recptnDt)로 중복된 열차(btrainNo) 제거
    realtimeArrivalList = filter_dup_realtime_arrival_list(
        realtime_arrival_list=realtimeArrivalList,
    )

    # 1. 상하행선
    # 2. 호선
    # 3. 남은 정거장 수 != 0
    realtimeArrivalList = filter(
        lambda realtime_json: lambda_realtime_arrival_list_filter(
            up_or_down=up_or_down,
            line_name=line_name,
            realtime_json=realtime_json,
        ),
        realtimeArrivalList,
    )

    # 남은 정거장수 적은순
    realtimeArrivalList = list(
        sorted(
            realtimeArrivalList,
            key=lambda realtime_json: lambda_realtime_arrival_list_sort(
                realtime_json=realtime_json,
            ),
        )
    )

    return realtimeArrivalList
