from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.domain.token.eb_token.sources.eb_token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional
from eb_fast_api.domain.schedule.sources.schedule_feature.create import (
    create_schedule as cs,
)
from eb_fast_api.domain.schedule.sources.schedule_feature.create import (
    create_notification as cn,
)
from eb_fast_api.domain.schedule.sources.schedule_feature.update import (
    update_schedule as us,
)
from eb_fast_api.domain.schedule.sources.schedule_feature.update import (
    update_notification as un,
)
from eb_fast_api.domain.schedule.sources.schedule_feature.delete import (
    delete_schedule as ds,
)
from eb_fast_api.domain.schedule.sources.schedule_feature.delete import (
    delete_notification as dn,
)
from eb_fast_api.service.notification.sources.provider.notification_schedule_provider import (
    noti_schedule_provider,
)
from eb_fast_api.service.notification.sources.provider.notification_transport_provider import (
    noti_transport_provider,
)
from eb_fast_api.snippets.sources.logger import logger
from eb_fast_api.snippets.sources import eb_datetime


router = APIRouter(prefix="/schedule")


@router.post("/create")
def create_schedule(
    scheduleInfo: ScheduleInfo,
    pathInfo: Optional[PathInfo] = None,
    userEmail=Depends(getUserEmail),
    session=Depends(EBDataBase.get_session),
    engine=Depends(EBDataBase.get_engine),
):
    scheduleInfo.time = scheduleInfo.time.replace(microsecond=0, tzinfo=None)

    try:
        cs.create_schedule(
            session=session,
            engine=engine,
            user_email=userEmail,
            schedule_info=scheduleInfo,
            path_info=pathInfo,
        )
    except Exception as e:
        logger.debug(f"schedule_router, create_schedule: {e}")
        # 다른 에러 상황은?
        raise HTTPException(
            status_code=400,
            detail="서버 스케줄 생성 에러",
        )

    now = eb_datetime.get_datetime_now()
    try:
        cn.create_notification_schedule(
            user_email=userEmail,
            schedule_info=scheduleInfo,
            noti_schedule_provider=noti_schedule_provider,
            now=now,
        )
    except Exception as e:
        logger.debug(f"schedule_router, create_notification_schedule: {e}")
        raise HTTPException(
            status_code=401,
            detail="스케줄 알림 생성 에러",
        )

    try:
        cn.create_notification_transport(
            user_email=userEmail,
            schedule_info=scheduleInfo,
            path_info=pathInfo,
            noti_transport_provider=noti_transport_provider,
            now=now,
        )
    except Exception as e:
        logger.debug(f"schedule_router, create_notification_transport: {e}")
        raise HTTPException(
            status_code=402,
            detail="배차 알림 생성 에러",
        )


@router.patch("/update")
def update_schedule(
    scheduleInfo: ScheduleInfo,
    pathInfo: Optional[PathInfo] = None,
    userEmail=Depends(getUserEmail),
    session=Depends(EBDataBase.get_session),
    engine=Depends(EBDataBase.get_engine),
):
    scheduleInfo.time = scheduleInfo.time.replace(microsecond=0, tzinfo=None)

    try:
        us.update_schedule(
            session=session,
            engine=engine,
            user_email=userEmail,
            schedule_info=scheduleInfo,
            path_info=pathInfo,
        )
    except Exception as e:
        logger.debug(f"schedule_router, update_schedule: {e}")
        # 다른 에러 상황은?
        raise HTTPException(
            status_code=400,
            detail="서버 스케줄 수정 에러",
        )

    now = eb_datetime.get_datetime_now()
    try:
        un.update_notification_schedule(
            user_email=userEmail,
            schedule_info=scheduleInfo,
            noti_schedule_provider=noti_schedule_provider,
            now=now,
        )
    except Exception as e:
        logger.debug(f"schedule_router, update_notification_schedule: {e}")
        raise HTTPException(
            status_code=401,
            detail="스케줄 알림 수정 에러",
        )

    try:
        un.update_notification_transport(
            user_email=userEmail,
            schedule_info=scheduleInfo,
            path_info=pathInfo,
            noti_transport_provider=noti_transport_provider,
            now=now,
        )
    except Exception as e:
        logger.debug(f"schedule_router, update_notification_transport: {e}")
        raise HTTPException(
            status_code=402,
            detail="배차 알림 수정 에러",
        )


@router.delete("/delete")
def delete_schedule(
    schedule_id: str,
    user_email=Depends(getUserEmail),
    session=Depends(EBDataBase.get_session),
    engine=Depends(EBDataBase.get_engine),
):
    try:
        ds.delete_schedule(
            session=session,
            engine=engine,
            user_email=user_email,
            schedule_id=schedule_id,
        )
    except Exception as e:
        logger.debug(f"schedule_router, delete_schedule: {e}")
        raise HTTPException(
            status_code=400,
            detail="스케줄 삭제 에러",
        )

    try:
        dn.delete_notification_schedule(
            schedule_id=schedule_id,
            noti_schedule_provider=noti_schedule_provider,
        )
    except Exception as e:
        logger.debug(f"schedule_router, delete_notification_schedule: {e}")
        raise HTTPException(
            status_code=401,
            detail="스케줄 알림 삭제 에러",
        )

    try:
        dn.delete_notification_transport(
            schedule_id=schedule_id,
            noti_transport_provider=noti_transport_provider,
        )
    except Exception as e:
        logger.debug(f"schedule_router, delete_notification_transport: {e}")
        raise HTTPException(
            status_code=402,
            detail="배차 알림 삭제 에러",
        )
