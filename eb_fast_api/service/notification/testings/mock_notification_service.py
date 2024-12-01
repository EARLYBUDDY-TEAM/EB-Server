from unittest.mock import patch
from eb_fast_api.service.notification.sources import notification_service
from typing import Optional
from eb_fast_api.database.sources.crud.cruds import UserCRUD


test_ios_token = "fkefvhXsAUMBiwaUoNZCCE:APA91bGi0oyAwI1Qx4AklaeqHiFawy2v5tH4m_8TRfe56cUcCAjLbLMT2sbcqSglp_Hx1suYoDj84C_E6voCiffgqVliOjNw71GbeO4261PkP4QjU9hnLI0"
test_android_token = "fkefvhXsAUMBiwaUoNZCCE:APA91bGi0oyAwI1Qx4AklaeqHiFawy2v5tH4m_8TRfe56cUcCAjLbLMT2sbcqSglp_Hx1suYoDj84C_E6voCiffgqVliOjNw71GbeO4261PkP4QjU9hnLI0"


def patcher_send_notification():
    def mock_send_notification(
        fcm_token: str,
        title: str,
        body: str,
    ):
        return

    patcher = patch.object(
        notification_service,
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
        notification_service,
        "get_fcm_token",
        new=mock_get_fcm_token,
    )
    return patcher
