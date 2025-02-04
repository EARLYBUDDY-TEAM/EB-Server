from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from eb_fast_api.service.notification.sources.feature.schedule.send_schedule_notification import (
    send_schedule_notification,
)
from eb_fast_api.service.notification.sources.feature.common.empty_and_add.empty_and_add_notification import (
    empty_and_add_all_user_notification,
)
from eb_fast_api.service.notification.sources.feature.transport.send_transport_notification import (
    send_transport_notification,
)
from apscheduler.triggers.cron import CronTrigger
from eb_fast_api.snippets.sources.eb_datetime import KST_HOUR
import asyncio


def add_job_send_transport_notification(scheduler):
    scheduler.add_job(
        lambda: asyncio.run(send_transport_notification()),
        "interval",
        minutes=1,
        # seconds=10,
    )


def add_job_send_schedule_notification(scheduler):
    scheduler.add_job(
        lambda: send_schedule_notification(),
        "interval",
        minutes=1,
        # seconds=10,
    )


def add_job_empty_notification(scheduler):
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

    background_scheduler = BackgroundScheduler()
    add_job_send_schedule_notification(
        scheduler=background_scheduler,
    )
    add_job_send_transport_notification(
        scheduler=background_scheduler,
    )
    add_job_empty_notification(
        scheduler=background_scheduler,
    )

    background_scheduler.start()
