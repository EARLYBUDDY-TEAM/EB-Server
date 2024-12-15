import pytest
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    BusRequestRealTimeInfo,
    SubwayRequestRealTimeInfo,
    NotificationTransport,
    NotificationTransportContent,
)
from eb_fast_api.service.notification.sources.feature.transport import (
    notification_transport_content as ntc,
)
from eb_fast_api.service.realtime.testings import mock_subway_realtime_service as msrs
from eb_fast_api.service.notification.testings import (
    mock_notification_transport_content_helper as mntch,
)
from eb_fast_api.service.notification.testings import (
    mock_notification_transport_content as mntc,
)


@pytest.mark.asyncio
async def test_make_subway_notification_body():
    # given
    subway_request_real_time_info = SubwayRequestRealTimeInfo.mock()
    station_name = "잠실"
    arrival_before = 10

    subway_arrival_info = (1234, 10)
    transport_number, arrival_minute = subway_arrival_info

    patcher_request = msrs.patcher_request()
    patcher_request.start()
    patcher_get_arrival_info = mntch.patcher_get_arrival_info(
        return_value=subway_arrival_info,
    )
    patcher_get_arrival_info.start()

    # when
    result = await ntc.make_subway_notification_body(
        subway_request_real_time_info=subway_request_real_time_info,
        station_name=station_name,
        arrival_before=arrival_before,
    )

    # then
    transport_type = "지하철"
    expect_result = f"{transport_type} {transport_number} {station_name} 도착까지 {arrival_minute}분 남았습니다."
    assert result == expect_result

    # teardown
    patcher_request.stop()
    patcher_get_arrival_info.stop()


@pytest.mark.asyncio
async def test_make_bus_notification_body():
    # given
    bus_request_real_time_info = BusRequestRealTimeInfo.mock()
    station_name = "잠실"
    arrival_before = 10

    bus_arrival_info = (1234, 10)
    transport_number, arrival_minute = bus_arrival_info

    patcher_request = msrs.patcher_request()
    patcher_request.start()
    patcher_get_arrival_info = mntch.patcher_get_arrival_info(
        return_value=bus_arrival_info,
    )
    patcher_get_arrival_info.start()

    # when
    result = await ntc.make_bus_notification_body(
        bus_request_real_time_info=bus_request_real_time_info,
        station_name=station_name,
        arrival_before=arrival_before,
    )

    # then
    transport_type = "버스"
    expect_result = f"{transport_type} {transport_number}번 {station_name} 도착까지 {arrival_minute}분 남았습니다."
    assert result == expect_result

    # teardown
    patcher_request.stop()
    patcher_get_arrival_info.stop()


@pytest.mark.asyncio
async def test_make_body_isinstance_SUBWAY():
    # given
    return_value = "subway"
    noti_transport = NotificationTransport.mock_subway()
    patcher = mntc.patcher_make_subway_notification_body(return_value=return_value)
    patcher.start()

    # when
    result = await ntc.make_body(
        noti_transport=noti_transport,
    )

    # then
    assert result == return_value

    # teardown
    patcher.stop()


@pytest.mark.asyncio
async def test_make_body_isinstance_BUS():
    # given
    return_value = "bus"
    noti_transport = NotificationTransport.mock_bus()
    patcher = mntc.patcher_make_bus_notification_body(return_value=return_value)
    patcher.start()

    # when
    result = await ntc.make_body(
        noti_transport=noti_transport,
    )

    # then
    assert result == return_value

    # teardown
    patcher.stop()
