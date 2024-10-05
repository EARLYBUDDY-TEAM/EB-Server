from fastapi import APIRouter, Depends, HTTPException
from typing import List
from eb_fast_api.domain.home.sources import home_feature
from eb_fast_api.domain.home.sources.home_schema import ScheduleCardList, ScheduleCard
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/home")


@router.get("/get_all_schedule_cards")
def get_all_schedule_cards(
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
    placeCRUD=Depends(EBDataBase.place.getCRUD),
) -> ScheduleCardList:
    scheduleList = home_feature.read_all_schedule(
        userEmail=userEmail,
        scheduleCRUD=scheduleCRUD,
    )

    cards: List[ScheduleCard] = [
        home_feature.schedule_to_schedulecard(
            schedule=schedule,
            placeCRUD=placeCRUD,
        )
        for schedule in scheduleList
    ]

    scheduleCardList = ScheduleCardList(scheduleCardList=cards)
    return scheduleCardList


@router.delete("/delete_schedule_card")
def delete_schedule_card(
    scheduleID: int,
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
):
    try:
        scheduleCRUD.delete(
            userEmail=userEmail,
            scheduleID=scheduleID,
        )
    except:
        raise HTTPException(
            status_code=400,
            detail="스케줄 삭제 에러",
        )
