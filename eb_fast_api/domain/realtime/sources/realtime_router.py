from fastapi import APIRouter, HTTPException
from eb_fast_api.domain.realtime.sources import realtime_feature
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfoList


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
