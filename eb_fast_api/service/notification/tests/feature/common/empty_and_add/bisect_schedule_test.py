from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    bisect_schedule as bs,
)
from eb_fast_api.database.sources.model.models import Schedule
from datetime import timedelta
from unittest import TestCase
from eb_fast_api.snippets.testings import mock_eb_datetime as med


class TestBisectSchedule(TestCase):
    schedule_dict_list = []
    now = med.mock_now

    @classmethod
    def setUpClass(cls):
        cls.patcher_get_datetime_now = med.patcher_get_datetime_now(
            return_value=med.mock_now,
        )
        cls.patcher_get_datetime_now.start()
        cls.now = med.mock_now

    @classmethod
    def tearDownClass(cls):
        cls.patcher_get_datetime_now.stop()
        cls.patcher_get_datetime_now = None

    def tearDown(self):
        self.schedule_dict_list = []

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
        left_index = bs.get_left_index(
            schedule_dict_list=self.schedule_dict_list,
            today_date=self.now.date(),
        )

        # then
        assert left_index == 5

    def test_bisect_right_schedule(self):
        # given
        self.create_sorted_schedule_dict_list()

        # when
        right_index = bs.get_right_index(
            schedule_dict_list=self.schedule_dict_list,
            today_date=self.now.date(),
        )

        # then
        assert right_index == 10
