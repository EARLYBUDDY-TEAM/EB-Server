from eb_fast_api.service.notification.sources.feature.common import fcm_feature as ff
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    noti_transport_provider,
)
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from eb_fast_api.service.notification.sources.feature.transport import (
    notification_transport_content as ntc,
)
from eb_fast_api.snippets.sources import eb_datetime


async def send_transport_notification(
    user_crud: UserCRUD,
    provider=noti_transport_provider,
):
    now = eb_datetime.get_datetime_now()
    logger.debug(f"START send_transport_notification, now : {now}")
    logger.debug(f"transport provider data count : {len(provider.data)}")

    noti_transport_list = provider.get_notification(now=now)

    for noti_transport in noti_transport_list:
        provider.add_notification(
            noti_schema=noti_transport,
            now=now,
        )

        body = await ntc.make_body(noti_transport=noti_transport)
        if body == None:
            continue

        user_email = noti_transport.user_email
        fcm_token = ff.get_fcm_token(
            user_crud=user_crud,
            user_email=user_email,
        )

        if not fcm_token:
            continue

        title = noti_transport.noti_content.schedule_name

        logger.debug("#################################")
        logger.debug("send_transport_notification")
        logger.debug(f"title : {title}")
        logger.debug(f"body : {body}")
        logger.debug(f"fcm_token : {fcm_token}")
        logger.debug("#################################")

        ff.send_notification(
            fcm_token=fcm_token,
            title=title,
            body=body,
        )
