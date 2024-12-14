from apscheduler.schedulers.background import BackgroundScheduler
from eb_fast_api.service.notification.sources.feature.send_schedule_notification import (
    send_schedule_notification,
)
from eb_fast_api.service.notification.sources.feature.empty_and_add_notification import (
    empty_and_add_all_user_notification,
)
from eb_fast_api.service.notification.sources.feature.transport.send_transport_notification import (
    send_transport_notification,
)
from apscheduler.triggers.cron import CronTrigger
from eb_fast_api.snippets.sources.eb_datetime import KST_HOUR
from datetime import datetime
from eb_fast_api.snippets.sources.eb_datetime import get_datetime_now


def add_job_send_transport_notification(
    now: datetime,
    scheduler: BackgroundScheduler,
):
    scheduler.add_job(
        lambda: send_transport_notification(now=now),
        "interval",
        minutes=1,
    )


def add_job_send_schedule_notification(
    now: datetime,
    scheduler: BackgroundScheduler,
):
    scheduler.add_job(
        lambda: send_schedule_notification(now=now),
        "interval",
        minutes=1,
    )


def add_job_empty_notification(
    scheduler: BackgroundScheduler,
):
    hour = 3 + KST_HOUR
    trigger = CronTrigger(
        hour=str(hour),
        minute="0",
        second="0",
        timezone=None,
    )
    scheduler.add_job(
        lambda: empty_and_add_all_user_notification(),
        trigger=trigger,
    )


def initialize_notification_scheduler():
    empty_and_add_all_user_notification()

    scheduler = BackgroundScheduler()
    now = get_datetime_now()
    add_job_send_schedule_notification(
        now=now,
        scheduler=scheduler,
    )

    # add_job_send_transport_notification(
    #     now=now,
    #     scheduler=scheduler,
    # )

    add_job_empty_notification(scheduler)
    scheduler.start()
