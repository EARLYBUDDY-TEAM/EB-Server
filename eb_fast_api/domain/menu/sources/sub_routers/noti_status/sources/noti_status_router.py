from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.snippets.sources import dictionary


router = APIRouter()


@router.get("/get")
def get_noti_status(
    user_email: str,
    userCRUD=Depends(EBDataBase.user.getCRUD),
) -> bool:
    user = userCRUD.read(email=user_email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="유저 정보가 없습니다",
        )

    is_notify = dictionary.safeDict(
        keyList=["is_notify"],
        fromDict=user,
    )

    return is_notify


@router.post("/enable")
def enable_noti_status(
    user_email: str,
    fcm_token=Security(
        APIKeyHeader(name="fcm-token"),
    ),
    userCRUD=Depends(EBDataBase.user.getCRUD),
):
    if not fcm_token:
        raise HTTPException(
            status_code=400,
            detail="FCM 토큰이 없습니다",
        )

    try:
        userCRUD.update(
            key_email=user_email,
            fcm_token=fcm_token,
            is_notify=True,
        )
        userCRUD.commit()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=401,
            detail="알림 가능 설정 실패",
        )


@router.post("/disable")
def disable_noti_status(
    user_email: str,
    userCRUD=Depends(EBDataBase.user.getCRUD),
):
    try:
        userCRUD.update(
            key_email=user_email,
            fcm_token="",
            is_notify=False,
        )
        userCRUD.commit()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=401,
            detail="알림 불가능 설정 실패",
        )
