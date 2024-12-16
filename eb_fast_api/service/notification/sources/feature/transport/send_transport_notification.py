from eb_fast_api.service.notification.sources.feature.common import fcm_feature as ff
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    noti_transport_provider,
)
from datetime import datetime
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.notification.sources.feature.transport import (
    notification_transport_content as ntc,
)
from eb_fast_api.snippets.sources import eb_datetime


async def send_transport_notification(
    provider=noti_transport_provider,
):
    now = eb_datetime.get_datetime_now()
    logger.debug(f"START send_transport_notification, now : {now}")
    logger.debug(f"transport provider data count : {len(provider.data)}")

    noti_transport_list = provider.get_notification(now=now)
    user_crud = EBDataBase.user.createCRUD()

    for noti_transport in noti_transport_list:
        noti_content = noti_transport.noti_content

        body = await ntc.make_body(noti_content=noti_content)
        if body == None:
            provider.add(noti_schema=noti_transport, now=now)
            continue

        user_email = noti_transport.user_email
        fcm_token = ff.get_fcm_token(
            user_crud=user_crud,
            user_email=user_email,
        )

        title = noti_content.schedule_name

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
