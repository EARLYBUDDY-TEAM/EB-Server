from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import APIKeyHeader
from eb_fast_api.database.sources.database import EBDataBase
from eb_fast_api.snippets.sources import dictionary


router = APIRouter(prefix="/token/fcm")


@router.get("/is_authorized")
def is_authorized(
    user_email: str,
    userCRUD=Depends(EBDataBase.user.getCRUD),
) -> bool:
    user = userCRUD.read(email=user_email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="유저 정보가 없습니다",
        )

    fcm_token = dictionary.safeDict(
        keyList=["fcm_token"],
        fromDict=user,
    )

    return False if not fcm_token else True


@router.post("/enable")
def update_fcm_token(
    user_email: str,
    fcm_token=Security(
        APIKeyHeader(name="fcm_token"),
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
        )
        userCRUD.commit()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=401,
            detail="FCM 토큰 업데이트 실패",
        )


@router.post("/disable")
def delete_fcm_token(
    user_email: str,
    userCRUD=Depends(EBDataBase.user.getCRUD),
):
    userCRUD.update(
        key_email=user_email,
        fcm_token="",
    )
    userCRUD.commit()
