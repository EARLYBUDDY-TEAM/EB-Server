from unittest.mock import patch
from eb_fast_api.service.notification.sources.feature import (
    send_schedule_notification as nsf,
)
from typing import Optional
from eb_fast_api.database.sources.crud.cruds import UserCRUD


def patcher_send_notification():
    def mock_send_notification(
        fcm_token: str,
        title: str,
        body: str,
    ):
        return

    patcher = patch.object(
        nsf,
        "send_notification",
        new=mock_send_notification,
    )
    return patcher


def patcher_get_fcm_token(return_value: Optional[str]):
    def mock_get_fcm_token(
        user_crud: UserCRUD,
        user_email: str,
    ) -> Optional[str]:
        return return_value

    patcher = patch.object(
        nsf,
        "get_fcm_token",
        new=mock_get_fcm_token,
    )
    return patcher
