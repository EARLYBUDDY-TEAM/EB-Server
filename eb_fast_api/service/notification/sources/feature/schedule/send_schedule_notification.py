from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    noti_schedule_provider,
)
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.service.notification.sources.feature import fcm_feature as ff
from datetime import datetime


def send_schedule_notification(
    now: datetime,
    provider=noti_schedule_provider,
):
    logger.debug(f"START send_schedule_notification, now : {now}")
    logger.debug(f"schedule provider data count : {len(provider.data)}")

    noti_schedule_list = provider.get_notification(now=now)
    user_crud = EBDataBase.user.createCRUD()
    for noti_schedule in noti_schedule_list:
        title = noti_schedule.schedule_name
        body = f"일정 시작 {noti_schedule.schedule_remain_time}분 전입니다."
        user_email = noti_schedule.user_email

        fcm_token = ff.get_fcm_token(
            user_crud=user_crud,
            user_email=user_email,
        )

        if fcm_token == None:
            return

        logger.debug("send_schedule_notification")
        logger.debug(f"title : {title}")
        logger.debug(f"body : {body}")

        ff.send_notification(
            fcm_token=fcm_token,
            title=title,
            body=body,
        )
    else:
        del user_crud
