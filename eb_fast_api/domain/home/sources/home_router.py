from fastapi import APIRouter, HTTPException, Depends
from eb_fast_api.domain.home.sources import home_feature
from eb_fast_api.domain.token.sources.token_feature import getUserEmail
from eb_fast_api.database.sources.database import EBDataBase


router = APIRouter(prefix="/home")


@router.get("/get_all_schedule")
def get_all_schedule(
    userEmail=Depends(getUserEmail),
    scheduleCRUD=Depends(EBDataBase.schedule.getCRUD),
):
    scheduleList = home_feature.read_all_schedule(
        userEmail=userEmail,
        scheduleCRUD=scheduleCRUD,
    )
