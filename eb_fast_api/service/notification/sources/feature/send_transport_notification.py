from eb_fast_api.service.notification.sources.feature import fcm_feature as ff
from eb_fast_api.service.notification.sources.schema.notification_transport import (
    NotificationTransportContent,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    noti_transport_provider,
)
from datetime import datetime
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional


def make_transport_notification_body(
    noti_content: NotificationTransportContent,
) -> Optional[str]:
    # {버스 or 지하철} {202번} {역 or 정류장} 도착까지 {30}분 남았습니다.
    return f"{noti_content.transport_type} {noti_content.station_name} 도착까지 {noti_content.arrival_before}분 남았습니다."


def send_transport_notification(
    now: datetime,
    provider=noti_transport_provider,
):
    logger.debug(f"START send_transport_notification, now : {now}")
    logger.debug(f"transport provider data count : {len(provider.data)}")
    noti_transport_list = provider.get_schedule(now=now)
    user_crud = EBDataBase.user.createCRUD()

    for noti_transport in noti_transport_list:
        noti_content = noti_transport.noti_content

        body = make_transport_notification_body(noti_content=noti_content)
        if body == None:
            continue

        title = noti_content.schedule_name

        user_email = noti_transport.user_email
        fcm_token = ff.get_fcm_token(
            user_crud=user_crud,
            user_email=user_email,
        )

        logger.debug("send_transport_notification")
        logger.debug(f"title : {title}")
        logger.debug(f"body : {body}")

        ff.send_notification(
            fcm_token=fcm_token,
            title=title,
            body=body,
        )
    else:
        del user_crud
