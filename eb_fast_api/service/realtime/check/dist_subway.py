from eb_fast_api.service.realtime.sources.realtime_service_schema import ArrivalInfo
from typing import Optional


def cal_current_subway_position(
    up_down: int,
    subway_position: str,
) -> tuple[str, int]:
    # return (next_subway_position, time_dist)
    return (subway_position, 1)


def cal_arrival_info() -> ArrivalInfo:
    pass


def add_dist(
    up_down: int,
    subway_position: str,
    time_gap: int,
) -> Optional[ArrivalInfo]:
    while 0 < time_gap:
        (next_subway_position, time_dist) = cal_current_subway_position(
            up_down=up_down,
            subway_position=subway_position,
        )
        if (time_gap - time_dist) < 0:  # trainSttus
            return cal_arrival_info()
        time_gap -= time_dist
        subway_position = next_subway_position

    return subway_position
