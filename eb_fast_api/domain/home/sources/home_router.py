from fastapi import APIRouter, Depends, HTTPException
from typing import List
from eb_fast_api.domain.home.sources import home_feature
from eb_fast_api.domain.home.sources.home_schema import (
    SchedulePathInfo,
    SchedulePathInfoList,
)
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/home")


@router.get("/get_all_schedules")
def get_all_schedules(
    userEmail=Depends(getUserEmail),
    session=Depends(EBDataBase.get_session),
) -> SchedulePathInfoList:
    schedule_dict_list = home_feature.read_all_schedule(
        session=session,
        userEmail=userEmail,
    )

    all_schedules: List[SchedulePathInfo] = [
        home_feature.schedule_dict_to_schedule_path_info(
            session=session,
            user_email=userEmail,
            schedule_dict=schedule_dict,
        )
        for schedule_dict in schedule_dict_list
    ]

    return SchedulePathInfoList(all_schedules=all_schedules)
