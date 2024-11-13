from eb_fast_api.domain.realtime.sources.realtime_schema import (
    SubwaySchedule,
    TotalSubwaySchedule,
)

mock_departure_time = "05:04"
mock_first_last_flag = 1

mock_subway_schedule_dict = {
    "subwayClass": 0,
    "departureTime": mock_departure_time,
    "startStationName": "구로",
    "endStationName": "천안",
    "firstLastFlag": mock_first_last_flag,
}

up_mock_search_subway_schedule_dict = {
    "result": {
        "weekdaySchedule": {"up": [mock_subway_schedule_dict]},
        "saturdaySchedule": {"up": [mock_subway_schedule_dict]},
        "holidaySchedule": {"up": [mock_subway_schedule_dict]},
    }
}


down_mock_search_subway_schedule_dict = {
    "result": {
        "weekdaySchedule": {"down": [mock_subway_schedule_dict]},
        "saturdaySchedule": {"down": [mock_subway_schedule_dict]},
        "holidaySchedule": {"down": [mock_subway_schedule_dict]},
    }
}


expect_subway_schedule = SubwaySchedule(
    departure_time=mock_departure_time,
    first_last_flag=mock_first_last_flag,
)

expect_total_subway_schedule = TotalSubwaySchedule(
    weekday_schedule=[expect_subway_schedule],
    saturday_schedule=[expect_subway_schedule],
    holiday_schedule=[expect_subway_schedule],
)
