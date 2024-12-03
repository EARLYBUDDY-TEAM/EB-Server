from pathlib import Path
import firebase_admin
from firebase_admin.messaging import Message
from eb_fast_api.service.notification.sources.notification_provider import (
    noti_schedule_provider,
)
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional
from eb_fast_api.snippets.sources import dictionary
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.snippets.sources.eb_datetime import get_datetime_now


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
    now = get_datetime_now()
    logger.debug(f"START send_schedule_notification, now : {now}")
    logger.debug(f"provider data count : {len(provider.data)}")

    noti_schedule_list = provider.get_schedule(now=now)
    user_crud = EBDataBase.user.createCRUD()
    for noti_schedule in noti_schedule_list:
        title = noti_schedule.schedule_name
        body = f"일정 시작 {noti_schedule.schedule_remain_time}분 전입니다."
        user_email = noti_schedule.user_email

        fcm_token = get_fcm_token(
            user_crud=user_crud,
            user_email=user_email,
        )

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
    else:
        del user_crud
