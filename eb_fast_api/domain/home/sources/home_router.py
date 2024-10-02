from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.home.sources import home_feature
from eb_fast_api.domain.home.sources.home_schema import ScheduleCard
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase
from typing import List

router = APIRouter(prefix="/home")


@router.get("/get_all_schedule_cards_data")
def get_all_schedule_cards_data(
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
) -> List[ScheduleCard]:
    scheduleList = home_feature.read_all_schedule(
        userEmail=userEmail,
        scheduleCRUD=scheduleCRUD,
    )

    scheduleCardList = [schedule for schedule in scheduleList]
    return scheduleCardList
