from fastapi import APIRouter, HTTPException
from eb_fast_api.service.realtime.sources.service import bus_realtime_service as bas
from eb_fast_api.service.realtime.sources.service import subway_realtime_service as sas
from eb_fast_api.domain.realtime.sources.realtime_schema import RealTimeInfoList
from eb_fast_api.domain.realtime.sources import realtime_feature


router = APIRouter(prefix="/realtime")


@router.get("/get_bus_realtime_info")
async def get_bus_realtime_info(
    station_id: int,
) -> RealTimeInfoList:
    try:
        result = await bas.request(station_id=station_id)
        return RealTimeInfoList(real_time_info_list=result)
    except Exception as e:
        if isinstance(e, bas.GetBusStationRealtimeInfoError):
            raise HTTPException(
                status_code=500,
                detail="오디세이 서버 오류",
            )
        elif isinstance(e, bas.DecodeRealtimeInfoListError):
            raise HTTPException(
                status_code=501,
                detail="디코딩 오류",
            )
        else:
            raise HTTPException(
                status_code=502,
                detail="알 수 없는 오류",
            )


@router.get("/get_subway_realtime_info")
async def get_subway_realtime_info(
    station_name: str,
    line_name: str,
    direction: int,
) -> RealTimeInfoList:
    try:
        response_json = await realtime_feature.get_seoul_subway_realtime_json(
            station_name=station_name,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="서울 지하철 실시간 정보 조회 오류",
        )

    try:
        real_time_info = sas.filter_subway_realtime_data(
            data=response_json,
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
