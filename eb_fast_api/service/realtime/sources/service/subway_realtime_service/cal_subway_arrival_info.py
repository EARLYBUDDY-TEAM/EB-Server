from eb_fast_api.service.realtime.sources.realtime_service_schema import (
    ArrivalInfo,
    RealTimeInfo,
)
from typing import Optional, List
from eb_fast_api.snippets.sources import dictionary, eb_datetime
from datetime import datetime, timedelta


time_format = "%Y-%m-%d %H:%M:%S"
bet_station_time = 60 * 2


def init_data_create_time() -> str:
    time = eb_datetime.get_datetime_now() - timedelta(seconds=30)
    return time.strftime(time_format)


def init_barvlDt(
    left_station: int,
) -> str:
    return str(left_station * bet_station_time)


def cal_left_station(
    left_station: int,
    diff_total_seconds: int,
) -> int:
    tmp_left_station = left_station - (diff_total_seconds // bet_station_time)
    return max(0, tmp_left_station)


def get_left_station(
    realtime_json: dict,
) -> int:
    ordkey = dictionary.safeDict(
        keyList=["ordkey"],
        fromDict=realtime_json,
    )
    return int(ordkey[2:5])


def cal_arrival_sec(
    barvlDt: str,
    data_create_time: str,
) -> tuple[int, int]:
    arrival_total_seconds = int(barvlDt)
    data_create_time = datetime.strptime(data_create_time, time_format)
    now = eb_datetime.get_datetime_now()
    diff = now - data_create_time
    diff_total_seconds = int(diff.total_seconds())
    arrival_sec = arrival_total_seconds - diff_total_seconds
    return (arrival_sec, diff_total_seconds)
    # barvlDt - abs(데이터 생성 시간 - 현재 시간)


def get_transport_plate(
    realtime_json: dict,
) -> Optional[str]:
    transport_plate = dictionary.safeDict(
        keyList=["btrainNo"],
        fromDict=realtime_json,
    )
    return transport_plate


def cal_arrival_info(
    realtime_json: dict,
) -> Optional[ArrivalInfo]:
    left_station = get_left_station(realtime_json=realtime_json)

    barvlDt = dictionary.safeDict(
        keyList=["barvlDt"],
        fromDict=realtime_json,
    )

    if barvlDt == None or barvlDt == "0":
        barvlDt = init_barvlDt(left_station=left_station)

    data_create_time = dictionary.safeDict(
        keyList=["recptnDt"],
        fromDict=realtime_json,
    )
    if data_create_time == None:
        data_create_time = init_data_create_time()

    arrival_sec, diff_total_seconds = cal_arrival_sec(
        barvlDt=barvlDt,
        data_create_time=data_create_time,
    )
    if arrival_sec <= -5:
        return None

    left_station = cal_left_station(
        left_station=left_station,
        diff_total_seconds=diff_total_seconds,
    )

    transport_plate = get_transport_plate(
        realtime_json=realtime_json,
    )

    return ArrivalInfo(
        transport_plate=transport_plate,
        arrival_sec=arrival_sec,
        left_station=left_station,
    )


def init_realtime_info(
    line_name: str,
    arrival_info_list: List[ArrivalInfo],
) -> RealTimeInfo:
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

    try:
        arrival_info1 = arrival_info_list[0]
        realtime_info.arrival_info1 = arrival_info1
    except:
        pass

    try:
        arrival_info2 = arrival_info_list[1]
        realtime_info.arrival_info2 = arrival_info2
    except:
        pass

    return realtime_info


def get_realtime_info(
    line_name: str,
    filter_subway_realtime_json_list: List[dict],
) -> RealTimeInfo:
    arrival_info_list = []

    for realtime_json in filter_subway_realtime_json_list:
        if len(arrival_info_list) == 2:
            break

        arrival_info = cal_arrival_info(realtime_json=realtime_json)
        if arrival_info is not None:
            arrival_info_list.append(arrival_info)

    realtime_info = init_realtime_info(
        line_name=line_name,
        arrival_info_list=arrival_info_list,
    )

    return realtime_info
