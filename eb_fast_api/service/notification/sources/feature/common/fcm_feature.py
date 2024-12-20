import firebase_admin
from firebase_admin.messaging import Message
from eb_fast_api.database.sources.crud.cruds import UserCRUD
from pathlib import Path
from typing import Optional
from eb_fast_api.snippets.sources import dictionary


## eb_fast_api/service/notification/fcm_oauth/fcm_oauth.json
fcm_oauth_json_path = (
    Path(__file__)
    .parent.parent.parent.parent.joinpath("fcm_oauth/fcm_oauth.json")
    .absolute()
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
