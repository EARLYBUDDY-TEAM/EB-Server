from fastapi import APIRouter, HTTPException
from eb_fast_api.domain.realtime.sources.realtime_feature import (
    realtime_feature,
    subway_realtime_feature,
)
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


@router.get("/get_subway_realtime_info")
async def get_subway_realtime_info(
    station_name: str,
    line_name: str,
    direction: int,
) -> RealTimeInfoList:
    try:
        response = await subway_realtime_feature.get_seoul_subway_realtime_info(
            station_name=station_name,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="서울 지하철 실시간 정보 조회 오류",
        )

    try:
        real_time_info = subway_realtime_feature.filter_subway_realtime_data(
            data=response.json(),
            line_name=line_name,
            direction=direction,
        )
        return RealTimeInfoList(real_time_info_list=[real_time_info])
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=501,
            detail="지하철 데이터 필터링 오류",
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
