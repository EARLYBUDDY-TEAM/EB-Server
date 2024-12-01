from eb_fast_api.service.notification.sources.notification_provider import (
    NotificationScheduleProvider,
)
from eb_fast_api.service.notification.sources.notification_schema import (
    NotificationSchedule,
)
import heapq


def test_notification_schedule_provider_add_delete():
    # given
    noti_schedule_provider = NotificationScheduleProvider()
    noti_schedule = NotificationSchedule.mock()

    # when, then
    noti_schedule_provider.add_schedule(noti_schedule=noti_schedule)
    assert noti_schedule_provider.data[0] == noti_schedule

    noti_schedule_provider.delete_schedule(id=noti_schedule.id)
    assert len(noti_schedule_provider.data) == 0


def test_notification_schedule_provider_get_schedule():
    def heap_to_list(tmp_heap) -> list:
        tmp_list = []

        while tmp_heap:
            tmp = heapq.heappop(tmp_heap)
            tmp_list.append(tmp)

        return tmp_list

    # given
    noti_schedule1 = NotificationSchedule.mock(schedule_remain_time=10)
    noti_schedule2 = NotificationSchedule.mock(schedule_remain_time=20)
    noti_schedule3 = NotificationSchedule.mock(schedule_remain_time=30)
    noti_schedule_list = [
        noti_schedule1,
        noti_schedule2,
        noti_schedule3,
    ]
    noti_schedule_provider = NotificationScheduleProvider()
    for noti_schedule in noti_schedule_list:
        noti_schedule_provider.add_schedule(noti_schedule=noti_schedule)

    # when
    noti_schedule = noti_schedule_provider.get_schedule()
    if noti_schedule != None:
        noti_schedule_list.remove(noti_schedule)

    # then
    heapq.heapify(noti_schedule_list)
    assert heap_to_list(noti_schedule_list) == heap_to_list(noti_schedule_provider.data)
