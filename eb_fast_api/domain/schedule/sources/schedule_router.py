from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.schedule.sources import schedule_feature
from eb_fast_api.domain.schema.sources.schemas import ScheduleInfo, PathInfo
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase
from typing import Optional


router = APIRouter(prefix="/schedule")


@router.post("/create")
async def create_schedule(
    scheduleInfo: ScheduleInfo,
    pathInfo: Optional[PathInfo] = None,
    userEmail=Depends(getUserEmail),
    session=Depends(EBDataBase.get_session),
):
    scheduleInfo.time = scheduleInfo.time.replace(microsecond=0, tzinfo=None)
    try:
        schedule_feature.create_schedule(
            session=session,
            userEmail=userEmail,
            scheduleInfo=scheduleInfo,
            pathInfo=pathInfo,
        )
    except Exception as e:
        print(e)
        # 다른 에러 상황은?
        raise HTTPException(
            status_code=400,
            detail="서버 스케줄 생성 에러",
        )


@router.post("/update")
def update_schedule(
    scheduleInfo: ScheduleInfo,
    pathInfo: Optional[PathInfo] = None,
    userEmail=Depends(getUserEmail),
    session=Depends(EBDataBase.get_session),
):
    scheduleInfo.time = scheduleInfo.time.replace(microsecond=0, tzinfo=None)
    try:
        schedule_feature.update_schedule(
            session=session,
            userEmail=userEmail,
            scheduleInfo=scheduleInfo,
            pathInfo=pathInfo,
        )
    except Exception as e:
        print(e)
        # 다른 에러 상황은?
        raise HTTPException(
            status_code=400,
            detail="서버 스케줄 수정 에러",
        )
