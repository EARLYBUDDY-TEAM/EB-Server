from fastapi import APIRouter, HTTPException
from eb_fast_api.service.realtime.sources.service import bus_realtime_service as brs
from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    subway_realtime_service as srs,
)
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfoList


router = APIRouter(prefix="/realtime")


@router.get("/get_bus_realtime_info")
async def get_bus_realtime_info(
    station_id: int,
) -> RealTimeInfoList:
    try:
        result = await brs.request(station_id=station_id)
        return RealTimeInfoList(real_time_info_list=result)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="오디세이 서버 오류",
        )


@router.get("/get_subway_realtime_info")
async def get_subway_realtime_info(
    station_name: str,
    line_name: str,
    direction: int,
) -> RealTimeInfoList:
    try:
        result = await srs.request(
            station_name=station_name,
            line_name=line_name,
            direction=direction,
        )
        return RealTimeInfoList(real_time_info_list=result)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="오디세이 서버 오류",
        )
