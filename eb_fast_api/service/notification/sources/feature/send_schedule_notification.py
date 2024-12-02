from fastapi import FastAPI
from pathlib import Path
import firebase_admin
from firebase_admin.messaging import Message
from apscheduler.schedulers.background import BackgroundScheduler
from eb_fast_api.service.notification.sources.notification_provider import (
    noti_schedule_provider,
)
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional
from eb_fast_api.snippets.sources import dictionary
from eb_fast_api.snippets.sources.logger import logger


## eb_fast_api/service/notification/fcm_oauth/fcm_oauth.json
fcm_oauth_json_path = (
    Path(__file__).parent.parent.parent.joinpath("fcm_oauth/fcm_oauth.json").absolute()
)
cred = firebase_admin.credentials.Certificate(fcm_oauth_json_path)
firebase_default_app = firebase_admin.initialize_app(cred)


def send_notification(
    fcm_token: str,
    title: str,
    body: str,
):
    message = Message(
        notification=firebase_admin.messaging.Notification(
            title=title,
            body=body,
        ),
        token=fcm_token,
    )
    response = firebase_admin.messaging.send(message)


def get_fcm_token(
    user_crud: UserCRUD,
    user_email: str,
) -> Optional[str]:
    user_dict = user_crud.read(email=user_email)

    fcm_token = dictionary.safeDict(
        keyList=["fcm_token"],
        fromDict=user_dict,
    )
    return fcm_token


def send_schedule_notification(
    provider=noti_schedule_provider,
):
    cur_noti_schedule = provider.get_schedule()
    if cur_noti_schedule == None:
        return

    title = cur_noti_schedule.schedule_name
    body = f"일정 시작 {cur_noti_schedule.schedule_remain_time}분 전입니다."
    user_email = cur_noti_schedule.user_email

    user_crud = EBDataBase.user.createCRUD()
    fcm_token = get_fcm_token(
        user_crud=user_crud,
        user_email=user_email,
    )
    del user_crud

    if fcm_token == None:
        return

    logger.debug("send_schedule_notification")
    logger.debug(f"title : {title}")
    logger.debug(f"body : {body}")

    send_notification(
        fcm_token=fcm_token,
        title=title,
        body=body,
    )
