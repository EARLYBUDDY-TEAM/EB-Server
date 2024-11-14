from fastapi import APIRouter, HTTPException
from eb_fast_api.domain.realtime.sources import realtime_feature
from eb_fast_api.domain.realtime.sources.realtime_schema import (
    RealTimeInfoList,
    TotalSubwaySchedule,
)


router = APIRouter(prefix="/realtime")


@router.get("/get_bus_realtime_info")
async def get_bus_realtime_info(
    station_id: int,
) -> RealTimeInfoList:
    try:
        response = await realtime_feature.get_bus_station_realtime_info(
            station_id=station_id,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="오디세이 서버 오류",
        )

    try:
        real_time_info_list = realtime_feature.decode_real_time_info_list(
            json=response.json()
        )
        return RealTimeInfoList(real_time_info_list=real_time_info_list)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=501,
            detail="디코딩 오류",
        )


@router.get("/get_total_subway_schedule")
async def get_total_subway_schedule(
    station_id: int,
    way_code: int,
) -> TotalSubwaySchedule:
    try:
        response = await realtime_feature.search_subway_schedule(
            station_id=station_id,
            way_code=way_code,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="오디세이 서버 오류",
        )

    try:
        total_subway_schedule = realtime_feature.subway_schedule_json_to_schema(
            way_code=way_code, json=response.json()
        )

        return total_subway_schedule
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=501,
            detail="디코딩 오류",
        )
