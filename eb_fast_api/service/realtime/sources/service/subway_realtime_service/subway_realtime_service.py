from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    subway_realtime_client as src,
)
from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    filter_subway_realtime_json as fsrj,
)
from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    cal_subway_arrival_info as csai,
)
from eb_fast_api.service.realtime.sources.realtime_service_schema import RealTimeInfo
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.service.realtime.check import json_helper as jh


# def save_realtime_info(
#     station_name: str,
#     save_dict: dict,
# ):
#     save_path = jh.filtered_json_name(
#         station_name=station_name,
#         now=eb_datetime.get_datetime_now(),
#     )
#     jh.save_dict_as_json_file(
#         save_path=save_path,
#         save_dict=save_dict,
#     )


async def request(
    station_name: str,
    line_name: str,
    up_or_down: int,
) -> RealTimeInfo:
    try:
        response = await src.get_seoul_subway_realtime_json(
            station_name=station_name,
        )
        response_json = response.json()
    except Exception as e:
        print(e)
        raise Exception("get_seoul_subway_realtime_info_error")

    filter_subway_realtime_json_list = fsrj.filter_subway_realtime_json(
        json=response_json,
        line_name=line_name,
        up_or_down=up_or_down,
    )

    realtime_info = csai.get_realtime_info(
        line_name=line_name,
        filter_subway_realtime_json_list=filter_subway_realtime_json_list,
    )

    return realtime_info
