from contextlib import asynccontextmanager
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from eb_fast_api.service.notification.sources.feature.send_schedule_notification import (
    send_schedule_notification,
)


@asynccontextmanager
async def notification_scheduler(app: FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        lambda: send_schedule_notification(),
        "interval",
        minutes=1,
    )
    scheduler.start()
    yield
