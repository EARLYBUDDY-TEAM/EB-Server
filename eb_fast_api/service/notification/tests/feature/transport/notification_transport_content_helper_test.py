from eb_fast_api.service.notification.sources.schema.notification_transport import (
    RequestRealTimeInfo,
)
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from eb_fast_api.service.notification.sources.feature.transport import (
    notification_transport_content_helper as ntch,
)


def test_is_transport_duplicate_RETURN_TRUE():
    # given
    realtime_info = RealTimeInfo.mock()
    request_real_time_info = RequestRealTimeInfo.mock()
    dup = request_real_time_info.dup
    transport_number = realtime_info.transport_number
    transport_plate = realtime_info.arrival_info1.transport_plate
    dup[transport_number] = transport_plate

    # when
    result = ntch.is_transport_duplicate(
        realtime_info=realtime_info,
        request_real_time_info=request_real_time_info,
    )

    # then
    assert result is True


def test_is_transport_duplicate_RETURN_FALSE():
    # given
    realtime_info = RealTimeInfo.mock()
    request_real_time_info = RequestRealTimeInfo.mock()

    # when
    result = ntch.is_transport_duplicate(
        realtime_info=realtime_info,
        request_real_time_info=request_real_time_info,
    )

    # then
    assert result is False


def test_get_arrival_info():
    # given
    realtime_info = RealTimeInfo.mock()
    realtime_info_list = [realtime_info]
    request_real_time_info = RequestRealTimeInfo.mock()
    arrival_minute = 10
    arrival_before = arrival_minute + 1
    realtime_info.arrival_info1.arrival_sec = arrival_minute * 60

    # when
    result = ntch.get_arrival_info(
        realtime_info_list=realtime_info_list,
        request_real_time_info=request_real_time_info,
        arrival_before=arrival_before,
    )

    # then
    exepct_result = (realtime_info.transport_number, arrival_minute)
    assert result == exepct_result
