from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    empty_and_add_notification as eaan,
)
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    NotificationTransportProvider,
)
from eb_fast_api.snippets.testings import mock_eb_datetime as med
from eb_fast_api.service.notification.testings import mock_notification_schedule as mns
from eb_fast_api.service.notification.testings import mock_notification_transport as mnt
from eb_fast_api.service.notification.sources.schema.notification_schedule import (
    NotificationSchedule,
)
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransport,
)
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.database.testings.mock_crud import mock_path_crud as mpc
from eb_fast_api.database.sources.database import EBDataBase


def test_add_notification_schedule_to_provider():
    # given
    mock_noti_schedule = NotificationSchedule.mock()
    now = eb_datetime.get_datetime_now()
    mock_noti_schedule.noti_time = eb_datetime.get_only_time(now)
    mock_schedule_dict = {
        "id": "test",
        "title": "test",
        "time": now,
        "notify_schedule": 0,
    }
    noti_schedule_provider = NotificationScheduleProvider()
    patcher_init = mns.patcher_init(return_value=mock_noti_schedule)
    patcher_init.start()

    # when
    eaan.add_notification_schedule_to_provider(
        user_email="",
        schedule_dict=mock_schedule_dict,
        noti_schedule_provider=noti_schedule_provider,
        now=now,
    )

    # then
    assert len(noti_schedule_provider.data) == 1
    assert noti_schedule_provider.data[0] == mock_noti_schedule

    # teardown
    patcher_init.stop()


def test_add_notification_transport_to_provider():
    # given
    now = eb_datetime.get_datetime_now()
    mock_schedule_dict = {
        "id": "test",
        "title": "test",
        "time": now,
        "notify_transport": 0,
        "notify_transport_range": 0,
    }
    mock_noti_transport = NotificationTransport.mock_bus()
    mock_noti_transport.noti_start_time = eb_datetime.get_only_time(now)
    mock_noti_transport.noti_end_time = eb_datetime.get_only_time(now)
    noti_transport_provider = NotificationTransportProvider()
    patcher_read = mpc.patcher_read(return_value={})
    patcher_read.start()
    patcher_init = mnt.patcher_init(return_value=mock_noti_transport)
    patcher_init.start()
    path_crud = EBDataBase.path.createCRUD()

    # when
    eaan.add_notification_transport_to_provider(
        user_email="",
        schedule_dict=mock_schedule_dict,
        noti_transport_provider=noti_transport_provider,
        path_crud=path_crud,
        now=now,
    )

    # then
    assert len(noti_transport_provider.data) == 1
    assert noti_transport_provider.data[0] == mock_noti_transport

    # teardown
    patcher_read.stop()
    patcher_init.stop()
