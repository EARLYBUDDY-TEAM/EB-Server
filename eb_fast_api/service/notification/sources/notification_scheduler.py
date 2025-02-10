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
from eb_fast_api.database.sources.database import EBDataBase


async def job_send_notification():
    user_crud = EBDataBase.user.createCRUD()
    user_crud.rollback()
    await send_transport_notification(
        user_crud=user_crud,
    )
    send_schedule_notification(
        user_crud=user_crud,
    )
    user_crud.session.close()
    del user_crud


def add_job_send_notification(scheduler):
    scheduler.add_job(
        lambda: asyncio.run(job_send_notification()),
        "interval",
        minutes=1,
        # seconds=5,
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


"""
Serial {
    sync, 1m, 'add_job_send_notification' {
        sync {
            usercrud.rollback()
        }
        async {
            send_schedule_notification()
            send_transport_notification()
        }
    }
    sync, 'add_job_empty_notification' {
        empty_and_add_all_user_notification()
    }
}
"""


def setup_notification_scheduler(scheduler):
    add_job_send_notification(
        scheduler=scheduler,
    )
    add_job_empty_notification(
        scheduler=scheduler,
    )


def initialize_notification_scheduler(scheduler):
    empty_and_add_all_user_notification()
    setup_notification_scheduler(scheduler)
