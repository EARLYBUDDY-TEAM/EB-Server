from typing import List
from datetime import datetime


def get_left_index(
    schedule_dict_list: List[dict],
    today_date: datetime,
) -> int:
    low, high = 0, len(schedule_dict_list)
    index = 0
    while low < high:
        mid = (low + high) // 2
        cur_schedule_date = schedule_dict_list[mid]["time"].date()
        if cur_schedule_date == today_date:
            index = mid
            high = mid - 1
        elif cur_schedule_date < today_date:
            low = mid + 1
        else:
            high = mid - 1

    return index


def get_right_index(
    schedule_dict_list: List[dict],
    today_date: datetime,
) -> int:
    low, high = 0, len(schedule_dict_list)
    index = high
    while low < high:
        mid = (low + high) // 2
        cur_schedule_date = schedule_dict_list[mid]["time"].date()
        if cur_schedule_date == today_date:
            index = mid + 1
            low = mid + 1
        elif cur_schedule_date < today_date:
            low = mid + 1
        else:
            high = mid

    return index
