from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransport,
)
from eb_fast_api.snippets.sources import eb_datetime
from datetime import timedelta, datetime
import heapq


def create_mock_noti_transport_noti_range(
    now: datetime,
    noti_range: int,
    noti_dist: int,
) -> NotificationTransport:
    noti_transport = NotificationTransport.mock_bus()
    noti_transport.noti_end_time = now + timedelta(minutes=noti_range)
    noti_transport.noti_end_time = now + timedelta(minutes=noti_dist)
    noti_transport.noti_end_time = eb_datetime.get_only_time(
        noti_transport.noti_end_time
    )
    noti_transport.noti_start_time = now - timedelta(minutes=noti_range)
    noti_transport.noti_start_time = now + timedelta(minutes=noti_dist)
    noti_transport.noti_start_time = eb_datetime.get_only_time(
        noti_transport.noti_start_time
    )
    return noti_transport


def test_add_notification():
    # given
    noti_transport_provider = NotificationTransportProvider()
    mock_now = eb_datetime.get_datetime_now()
    noti_range = 5
    noti_dist = noti_range - 10
    noti_transport1 = create_mock_noti_transport_noti_range(
        now=mock_now,
        noti_range=noti_range,
        noti_dist=noti_dist,
    )
    noti_transport2 = create_mock_noti_transport_noti_range(
        now=mock_now,
        noti_range=noti_range,
        noti_dist=0,
    )

    assert len(noti_transport_provider.data) == 0

    # when
    add_result1 = noti_transport_provider.add_notification(
        noti_schema=noti_transport1,
        now=mock_now,
    )
    add_result2 = noti_transport_provider.add_notification(
        noti_schema=noti_transport2,
        now=mock_now,
    )

    # then
    assert add_result1 is False
    assert add_result2 is True
    assert len(noti_transport_provider.data) == 1
    assert noti_transport_provider.data[0] == noti_transport2


def test_get_notification():
    # given
    noti_transport_provider = NotificationTransportProvider()
    mock_now = eb_datetime.get_datetime_now()
    noti_range = 5
    noti_dist = noti_range + 10
    noti_transport1 = create_mock_noti_transport_noti_range(
        now=mock_now,
        noti_range=noti_range,
        noti_dist=0,
    )
    noti_transport2 = create_mock_noti_transport_noti_range(
        now=mock_now,
        noti_range=noti_range,
        noti_dist=noti_dist,
    )
    noti_transport_provider.data = [
        noti_transport1,
        noti_transport2,
    ]
    heapq.heapify(noti_transport_provider.data)

    # when
    noti_transport_list = noti_transport_provider.get_notification(now=mock_now)

    # then
    assert noti_transport_provider.data[0] == noti_transport2
    assert noti_transport_list[0] == noti_transport1
