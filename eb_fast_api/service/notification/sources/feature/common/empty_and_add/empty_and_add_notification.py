from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    noti_schedule_provider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    noti_transport_provider,
)
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from typing import List
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.service.notification.sources.feature.common.empty_and_add import (
    add_notification_to_provider as antp,
)
from eb_fast_api.snippets.sources.logger import logger


def get_all_user(
    user_crud: UserCRUD,
) -> List[dict]:
    return user_crud.read_all()


def empty_and_add_all_user_notification(
    noti_schedule_provider=noti_schedule_provider,
    noti_transport_provider=noti_transport_provider,
    session=EBDataBase.create_session(),
    engine=EBDataBase.create_engine(),
):
    user_crud = EBDataBase.user.createCRUD(
        session=session,
        engine=engine,
    )
    schedule_crud = EBDataBase.schedule.createCRUD(
        session=session,
        engine=engine,
    )
    path_crud = EBDataBase.path.createCRUD(
        session=session,
        engine=engine,
    )
    all_users = get_all_user(user_crud=user_crud)

    noti_schedule_provider.data = []
    noti_transport_provider.data = []

    for user in all_users:
        user_email = user["email"]

        logger.debug("--------------------------------")
        logger.debug(f"{user_email} START add_notification_to_provider")
        logger.debug("")

        antp.add_notification_to_provider(
            user_email=user_email,
            schedule_crud=schedule_crud,
            path_crud=path_crud,
            noti_schedule_provider=noti_schedule_provider,
            noti_transport_provider=noti_transport_provider,
        )

        logger.debug("")
        logger.debug(f"{user_email} END add_notification_to_provider")
        logger.debug("--------------------------------")
