from eb_fast_api.snippets.sources.eb_datetime import (
    KST_HOUR,
    get_datetime_now,
)
from datetime import timedelta
from apscheduler.triggers.cron import CronTrigger


def test_set_timezone_to_apns_scheduler():
    # given
    hour = 3 + KST_HOUR
    trigger = CronTrigger(
        hour=str(hour),
        minute="0",
        second="0",
        timezone=None,
    )

    # when
    previous_fire_time = get_datetime_now().replace(
        hour=hour,
        minute=0,
        second=0,
        microsecond=0,
    )
    hour_1 = previous_fire_time - timedelta(hours=1)
    hour_4 = previous_fire_time + timedelta(hours=1)

    expected_fire_time = previous_fire_time

    hour_1_fire_time = trigger.get_next_fire_time(
        previous_fire_time=previous_fire_time - timedelta(days=1),
        now=hour_1,
    ).replace(tzinfo=None)
    hour_4_fire_time = trigger.get_next_fire_time(
        previous_fire_time=previous_fire_time,
        now=hour_4,
    ).replace(tzinfo=None)

    # then
    assert hour_1_fire_time == expected_fire_time
    assert hour_4_fire_time == expected_fire_time + timedelta(days=1)
