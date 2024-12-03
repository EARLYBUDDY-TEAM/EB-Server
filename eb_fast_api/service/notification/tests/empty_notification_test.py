from eb_fast_api.service.notification.sources.feature.empty_and_add_notification import (
    bisect_left_schedule,
    bisect_right_schedule,
    add_today_schedule_notification,
    get_all_user,
)
from eb_fast_api.database.sources.model.models import Schedule
from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.database.testings.mock_crud import mock_schedule_crud as msc
from eb_fast_api.database.testings.mock_crud import mock_user_crud as muc
from datetime import timedelta
from unittest import TestCase
from eb_fast_api.snippets.testings import mock_eb_datetime as med


class TestEmptyNotification(TestCase):
    schedule_dict_list = []
    provider = NotificationScheduleProvider()

    now = med.mock_now

    @classmethod
    def setUpClass(cls):
        cls.patcher_get_datetime_now = med.patcher_get_datetime_now()
        cls.patcher_get_datetime_now.start()

    @classmethod
    def tearDownClass(cls):
        cls.patcher_get_datetime_now.stop()
        cls.patcher_get_datetime_now = None

    def tearDown(self):
        self.schedule_dict_list = []
        self.provider.data = []

    def create_sorted_schedule_dict_list(self):
        tmp_schedule_list = []

        for i in range(1, 6):
            mock_schedule = Schedule.mock()
            mock_schedule.time = self.now - timedelta(days=i)
            mock_schedule.notify_schedule = 0
            tmp_schedule_list.append(mock_schedule.to_dict())

        for _ in range(1, 6):
            mock_schedule = Schedule.mock()
            mock_schedule.time = self.now
            mock_schedule.notify_schedule = 0
            tmp_schedule_list.append(mock_schedule.to_dict())

        for i in range(1, 6):
            mock_schedule = Schedule.mock()
            mock_schedule.time = self.now + timedelta(days=i)
            mock_schedule.notify_schedule = 0
            tmp_schedule_list.append(mock_schedule.to_dict())

        self.schedule_dict_list = tmp_schedule_list

    def create_sorted_schedule_dict_list_not_exist_today(self):
        tmp_schedule_list = []

        for i in range(1, 6):
            mock_schedule = Schedule.mock()
            mock_schedule.time = self.now - timedelta(days=i)
            mock_schedule.notify_schedule = 0
            tmp_schedule_list.append(mock_schedule.to_dict())

        for i in range(1, 6):
            mock_schedule = Schedule.mock()
            mock_schedule.time = self.now + timedelta(days=i)
            mock_schedule.notify_schedule = 0
            tmp_schedule_list.append(mock_schedule.to_dict())

        self.schedule_dict_list = tmp_schedule_list

    def test_bisect_left_schedule(self):
        # given
        self.create_sorted_schedule_dict_list()

        # when
        left_index = bisect_left_schedule(
            schedule_dict_list=self.schedule_dict_list,
            today_date=self.now.date(),
        )

        # then
        assert left_index == 5

    def test_bisect_right_schedule(self):
        # given
        self.create_sorted_schedule_dict_list()

        # when
        right_index = bisect_right_schedule(
            schedule_dict_list=self.schedule_dict_list,
            today_date=self.now.date(),
        )

        # then
        assert right_index == 10

    def test_add_today_schedule_notification_exist_today_schedule(self):
        # given
        schedule_crud = EBDataBase.schedule.createCRUD()
        self.create_sorted_schedule_dict_list()
        patcher = msc.patcher_schedule_crud_read_all(
            return_value=self.schedule_dict_list,
        )
        patcher.start()

        # when
        add_today_schedule_notification(
            user_email="",
            schedule_crud=schedule_crud,
            noti_schedule_provider=self.provider,
        )

        # then
        assert len(self.provider.data) == 5

        # teardown
        patcher.stop()

    def test_empty_notification_not_exist_today_schedule(self):
        # given
        schedule_crud = EBDataBase.schedule.createCRUD()
        self.create_sorted_schedule_dict_list_not_exist_today()
        patcher = msc.patcher_schedule_crud_read_all(
            return_value=self.schedule_dict_list,
        )
        patcher.start()

        # when
        add_today_schedule_notification(
            user_email="",
            schedule_crud=schedule_crud,
            noti_schedule_provider=self.provider,
        )

        # then
        assert len(self.provider.data) == 0

        # teardown
        patcher.stop()

    def test_get_all_user(self):
        # given
        user_crud = EBDataBase.user.createCRUD()
        return_value = [{"test": "test"}]
        patcher = muc.patcher_read_all(return_value=return_value)
        patcher.start()

        # when, then
        all_user = get_all_user(user_crud=user_crud)
        assert all_user == return_value

        # teardown
        patcher.stop()
