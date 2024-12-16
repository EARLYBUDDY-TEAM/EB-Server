from eb_fast_api.domain.schedule.sources.schedule_feature.create import (
    create_notification as cns,
)
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from uuid import uuid4
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.testings import (
    mock_add_notification_provider as manp,
)
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)


def test_create_notification_transport():
    # given
    patcher_prepare_add_noti_transport_to_provider = (
        manp.patcher_prepare_add_noti_transport_to_provider(
            return_value=True,
        )
    )
    patcher_add_notification_transport_to_provider = (
        manp.patcher_add_notification_transport_to_provider(
            return_value=True,
        )
    )

    patcher_prepare_add_noti_transport_to_provider.start()
    patcher_add_notification_transport_to_provider.start()
    now = eb_datetime.get_datetime_now()

    # when
    result = cns.create_notification_transport(
        user_email="test@test.com",
        schedule_info=ScheduleInfo.mock(id=str(uuid4())),
        path_info=PathInfo.mock(),
        noti_transport_provider=NotificationTransportProvider(),
        now=now,
    )

    # then
    assert result is True

    # teardown
    patcher_add_notification_transport_to_provider.stop()
    patcher_prepare_add_noti_transport_to_provider.stop()


def test_create_notification_schedule():
    # given
    patcher_add_notification_schedule_to_provider = (
        manp.patcher_add_notification_schedule_to_provider(
            return_value=True,
        )
    )
    patcher_prepare_add_noti_transport_to_provider = (
        manp.patcher_prepare_add_noti_transport_to_provider(
            return_value=True,
        )
    )
    patcher_add_notification_schedule_to_provider.start()
    patcher_prepare_add_noti_transport_to_provider.start()
    now = eb_datetime.get_datetime_now()

    # when
    result = cns.create_notification_schedule(
        user_email="test@test.com",
        schedule_info=ScheduleInfo.mock(id=str(uuid4())),
        noti_schedule_provider=NotificationScheduleProvider(),
        now=now,
    )

    # then
    assert result is True

    # teardown
    patcher_add_notification_schedule_to_provider.stop()
    patcher_prepare_add_noti_transport_to_provider.stop()
