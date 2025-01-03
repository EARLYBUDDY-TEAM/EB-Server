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
        if (
            is_same_direction(
                up_or_down=up_or_down,
                realtime_json=realtime_json,
            )
            and is_same_line_name(
                line_name=line_name,
                realtime_json=realtime_json,
            )
            and is_left_station_not_zero(
                realtime_json=realtime_json,
            )
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


# def cal_arrival_sec(realtime_json: dict) -> Optional[int]:
#     arrival_sec = None
#     data_create_time = dictionary.safeDict(
#         keyList=["recptnDt"],
#         fromDict=realtime_json,
#     )
#     arrival_remain_time = dictionary.safeDict(
#         keyList=["barvlDt"],
#         fromDict=realtime_json,
#     )

#     if (data_create_time != None) and (arrival_remain_time != None):
#         data_create_time = datetime.strptime(data_create_time, "%Y-%m-%d %H:%M:%S")
#         now = get_date_time_now()
#         diff = now - data_create_time
#         diff_total_seconds = int(diff.total_seconds())
#         arrival_sec = diff_total_seconds + int(arrival_remain_time)
#         # 남은 시간 + abs(데이터 생성 시간 - 현재 시간)

#     return arrival_sec


# def get_realtimeArrivalList(
#     json: dict,
# ) -> List[dict]:
#     return dictionary.safeDict(
#         keyList=["realtimeArrivalList"],
#         fromDict=json,
#     )


# def filter_subway_realtime_json(
#     json: dict,
#     line_name: str,
#     direction: int,
# ) -> List[dict]:
#     realtimeArrivalList = get_realtimeArrivalList(json=json)
#     tmp_filtered = []

#     for realtime_json in realtimeArrivalList:
#         if not is_same_line_name(
#             line_name=line_name,
#             realtime_json=realtime_json,
#         ):
#             continue

#         ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtime_json)
#         if not ordkey:
#             continue

#         if not is_same_direction(
#             direction=direction,
#             ordkey=ordkey,
#         ):
#             continue

#         tmp_filtered.append(realtime_json)

#     return tmp_filtered


# def get_subway_arrival_info_list(
#     filtered_realtime_json_list: List[dict],
# ) -> List[ArrivalInfo]:
#     arrival_info_list = []

#     for realtime_json in filtered_realtime_json_list:
#         ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtime_json)
#         if not ordkey:
#             continue

#         rota = ordkey[1]
#         transport_plate = dictionary.safeDict(
#             keyList=["btrainNo"], fromDict=realtime_json
#         )
#         left_station = int(ordkey[2:5])
#         arrival_sec = cal_arrival_sec(realtime_json=realtime_json)
#         arrival_info = ArrivalInfo(
#             transport_plate=transport_plate,
#             arrival_sec=arrival_sec,
#             left_station=left_station,
#         )
#         if rota == "1":
#             arrival_info_list.append(arrival_info)
#         elif rota == "2":
#             arrival_info_list.append(arrival_info)

#     return arrival_info_list


# if not realtimeArrivalList:
#     return []

# filtered_realtime_json_list = filter_subway_realtime_json(
#     data=data,
#     line_name=line_name,
#     direction=direction,
# )

# realtime_info = RealTimeInfo(
#     transport_number=line_name,
#     arrival_info1=ArrivalInfo(
#         transport_plate=None,
#         arrival_sec=None,
#         left_station=None,
#     ),
#     arrival_info2=ArrivalInfo(
#         transport_plate=None,
#         arrival_sec=None,
#         left_station=None,
#     ),
# )

# for realtime_json in realtimeArrivalList:
#     if (
#         not realtime_info.arrival_info1.is_optional()
#         and not realtime_info.arrival_info2.is_optional()
#     ):
#         print("return realtime_info")
#         print(f"realtime_info: {realtime_info}")
#         return realtime_info

#     if not is_same_line_name(
#         line_name=line_name,
#         realtime_json=realtime_json,
#     ):
#         continue

#     ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtime_json)
#     if ordkey is None:
#         continue

#     if not is_same_direction(
#         direction=direction,
#         ordkey=ordkey,
#     ):
#         continue

#     try:
#         left_station = int(ordkey[2:5])
#         arrival_sec = cal_arrival_sec(realtime_json=realtime_json)
#         transport_plate = dictionary.safeDict(
#             keyList=["btrainNo"], fromDict=realtime_json
#         )

#         rota = ordkey[1]
#         print(f"rota: {rota}")
#         print(f"left_station: {left_station}")
#         print(f"arrival_sec: {arrival_sec}")
#         print(f"transport_plate: {transport_plate}")

#         if rota == "1":
#             realtime_info.arrival_info1.left_station = left_station
#             realtime_info.arrival_info1.arrival_sec = arrival_sec
#             realtime_info.arrival_info1.transport_plate = transport_plate
#         elif rota == "2":
#             realtime_info.arrival_info2.left_station = left_station
#             realtime_info.arrival_info2.arrival_sec = arrival_sec
#             realtime_info.arrival_info2.transport_plate = transport_plate
#     except Exception as e:
#         print(e)
#         continue

# return realtime_info


# def filter_subway_realtime_json(
#     data: dict,
#     line_name: str,
#     direction: int,
# ) -> RealTimeInfo:
#     realtimeArrivalList = dictionary.safeDict(
#         keyList=["realtimeArrivalList"], fromDict=data
#     )

#     realtime_info = RealTimeInfo(
#         transport_number=line_name,
#         arrival_info1=ArrivalInfo(
#             transport_plate=None,
#             arrival_sec=None,
#             left_station=None,
#         ),
#         arrival_info2=ArrivalInfo(
#             transport_plate=None,
#             arrival_sec=None,
#             left_station=None,
#         ),
#     )

#     for realtime_json in realtimeArrivalList:
#         if (
#             not realtime_info.arrival_info1.is_optional()
#             and not realtime_info.arrival_info2.is_optional()
#         ):
#             print("return realtime_info")
#             print(f"realtime_info: {realtime_info}")
#             return realtime_info

#         if not is_same_line_name(
#             line_name=line_name,
#             realtime_json=realtime_json,
#         ):
#             continue

#         ordkey = dictionary.safeDict(keyList=["ordkey"], fromDict=realtime_json)
#         if ordkey is None:
#             continue

#         if not is_same_direction(
#             direction=direction,
#             ordkey=ordkey,
#         ):
#             continue

#         try:
#             left_station = int(ordkey[2:5])
#             arrival_sec = cal_arrival_sec(realtime_json=realtime_json)
#             transport_plate = dictionary.safeDict(
#                 keyList=["btrainNo"], fromDict=realtime_json
#             )

#             rota = ordkey[1]
#             print(f"rota: {rota}")
#             print(f"left_station: {left_station}")
#             print(f"arrival_sec: {arrival_sec}")
#             print(f"transport_plate: {transport_plate}")

#             if rota == "1":
#                 realtime_info.arrival_info1.left_station = left_station
#                 realtime_info.arrival_info1.arrival_sec = arrival_sec
#                 realtime_info.arrival_info1.transport_plate = transport_plate
#             elif rota == "2":
#                 realtime_info.arrival_info2.left_station = left_station
#                 realtime_info.arrival_info2.arrival_sec = arrival_sec
#                 realtime_info.arrival_info2.transport_plate = transport_plate
#         except Exception as e:
#             print(e)
#             continue

#     return realtime_info


# def filter_subway_realtime_data(
#     data: dict,
#     line_name: str,
#     direction: int,
# ) -> RealTimeInfo:
#     return RealTimeInfo.mock()


# async def request(
#     station_name: str,
#     line_name: str,
#     direction: int,
# ) -> List[RealTimeInfo]:
#     try:
#         response = await get_seoul_subway_realtime_info(
#             station_name=station_name,
#         )
#         response_json = response.json()
#     except Exception as e:
#         print(e)
#         raise Exception("get_seoul_subway_realtime_info_error")

#     real_time_info = filter_subway_realtime_data(
#         data=response_json,
#         line_name=line_name,
#         direction=direction,
#     )
#     return [real_time_info]
