from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransport,
    SubwayRequestRealTimeInfo,
    BusRequestRealTimeInfo,
)
from typing import Optional
from datetime import datetime, timedelta
from eb_fast_api.snippets.testings import mock_eb_datetime as med
from eb_fast_api.snippets.sources import eb_datetime


def create_mock_walk():
    return {
        "type": 3,
        "time": 100,
        "startName": "create_mock_walk",
        "way_code": "mock_way_code",
    }


def create_mock_bus(
    bus: BusRequestRealTimeInfo,
):
    return {
        "type": 2,
        "start_station_id": bus.station_id,
        "startName": bus.station_name,
    }


def create_mock_subway_path(
    subway: SubwayRequestRealTimeInfo,
):
    return {
        "type": 1,
        "startName": subway.station_name,
        "transports": [{"subwayType": subway.line_name}],
        "way_code": subway.direction,
    }


def create_mock_subpath_list():
    return [{}]


def test_get_request_real_time_info_subway():
    # given
    expect_subway_realtimeinfo = SubwayRequestRealTimeInfo.mock()
    subway_path_dict = create_mock_subway_path(expect_subway_realtimeinfo)
    mock_subpath_list = [
        create_mock_walk(),
        create_mock_walk(),
        subway_path_dict,
        create_mock_walk(),
    ]

    # when
    request_real_time_info = NotificationTransport.get_request_real_time_info(
        subpath_list=mock_subpath_list,
    )

    assert request_real_time_info == expect_subway_realtimeinfo


def test_get_request_real_time_info_bus():
    # given
    expect_bus_realtimeinfo = BusRequestRealTimeInfo.mock()
    bus_path_dict = create_mock_bus(expect_bus_realtimeinfo)
    mock_subpath_list = [
        create_mock_walk(),
        create_mock_walk(),
        bus_path_dict,
        create_mock_walk(),
    ]

    # when
    request_real_time_info = NotificationTransport.get_request_real_time_info(
        subpath_list=mock_subpath_list,
    )

    assert request_real_time_info == expect_bus_realtimeinfo


def test_get_request_real_time_info_subway_is_none():
    # given
    expect_subway_realtimeinfo = SubwayRequestRealTimeInfo.mock()
    subway_path_dict = create_mock_subway_path(expect_subway_realtimeinfo)
    subway_path_dict["transports"] = []
    mock_subpath_list = [
        create_mock_walk(),
        create_mock_walk(),
        subway_path_dict,
        create_mock_walk(),
    ]

    # when
    request_real_time_info = NotificationTransport.get_request_real_time_info(
        subpath_list=mock_subpath_list,
    )

    assert request_real_time_info == None


def test_cal_noti_start_end_time_FAIL_not_today():
    # given
    mock_now = med.mock_now
    pather = med.patcher_get_datetime_now(return_value=mock_now)
    pather.start()
    schedule_time: datetime = mock_now + timedelta(days=1)
    notify_transport_range: Optional[int] = 0

    # when
    noti_start_end_time = NotificationTransport.cal_noti_start_end_time(
        schedule_time=schedule_time,
        path_time=10,
        notify_transport_range=notify_transport_range,
        now=mock_now,
    )

    assert noti_start_end_time == None
    pather.stop()


def test_cal_noti_start_end_time_FAIL_out_of_schedule_time():
    # given
    mock_now = med.mock_now
    pather = med.patcher_get_datetime_now(return_value=mock_now)
    pather.start()
    schedule_time: datetime = mock_now - timedelta(minutes=1)
    notify_transport_range: Optional[int] = 0

    # when
    noti_start_end_time = NotificationTransport.cal_noti_start_end_time(
        schedule_time=schedule_time,
        path_time=10,
        notify_transport_range=notify_transport_range,
        now=mock_now,
    )

    assert noti_start_end_time == None
    pather.stop()


def test_cal_noti_start_end_time():
    # given
    mock_now = med.mock_now
    pather = med.patcher_get_datetime_now(return_value=mock_now)
    pather.start()
    schedule_time: datetime = mock_now + timedelta(hours=3)
    notify_transport_range: Optional[int] = 30
    path_time = 10
    # when
    noti_start_end_time = NotificationTransport.cal_noti_start_end_time(
        schedule_time=schedule_time,
        path_time=path_time,
        notify_transport_range=notify_transport_range,
        now=mock_now,
    )

    expect_start_time = schedule_time - timedelta(minutes=path_time)
    expect_noti_start_time = expect_start_time - timedelta(
        minutes=notify_transport_range
    )
    expect_noti_start_time = eb_datetime.get_only_time(expect_noti_start_time)
    expect_noti_end_time = expect_start_time
    expect_noti_end_time = eb_datetime.get_only_time(expect_noti_end_time)
    expect_noti_start_end_time = (expect_noti_start_time, expect_noti_end_time)
    assert noti_start_end_time == expect_noti_start_end_time
    pather.stop()


# def test_init_SUCCESS():
#     # given
#     from eb_fast_api.service.notification.testings.mock_notification_transport import (
#         user_email,
#         schedule_id,
#         schedule_name,
#         schedule_time,
#         notify_transport,
#         notify_transport_range,
#         path_dict,
#         now,
#     )

#     path_data = dictionary.safeDict(["data"], path_dict)
#     if path_data == None:
#         assert False

#     path_time = dictionary.safeDict(["time"], path_data)
#     if path_time == None:
#         assert False

#     # when
#     # notification_transport = NotificationTransport.init(
#     #     user_email=user_email,
#     #     schedule_id=schedule_id,
#     #     schedule_name=schedule_name,
#     #     schedule_time=schedule_time,
#     #     notify_transport=notify_transport,
#     #     notify_transport_range=notify_transport_range,
#     #     path_dict=path_dict,
#     #     now=now,
#     # )

#     # # then
#     # expect_notification_transport = NotificationTransport(
#     #     schedule_id=schedule_id,
#     #     user_email=user_email,
#     #     noti_content=NotificationTransportContent(
#     #         schedule_name=schedule_name,
#     #         arrival_before=notify_transport,
#     #         transport_type=transport_type,
#     #     ),
#     #     noti_start_time=noti_start_time,
#     #     noti_end_time=noti_end_time,
#     #     request_realtime_info=request_realtime_info,
#     # )
