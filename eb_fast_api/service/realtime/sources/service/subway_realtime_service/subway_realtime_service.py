from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    subway_realtime_client as src,
)
from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    filter_subway_realtime_json as fsrj,
)
from eb_fast_api.service.realtime.check import json_helper as jh


async def request(
    station_name: str,
    line_name: str,
    up_or_down: int,
):
    try:
        response = await src.get_seoul_subway_realtime_json(
            station_name=station_name,
        )
        response_json = response.json()
    except Exception as e:
        print(e)
        raise Exception("get_seoul_subway_realtime_info_error")

    result = fsrj.filter_subway_realtime_json(
        json=response_json,
        line_name=line_name,
        up_or_down=up_or_down,
    )

    save_path = jh.filtered_json_name(
        station_name=station_name,
        now=fsrj.get_date_time_now(),
    )
    jh.save_dict_as_json_file(
        save_path=save_path,
        save_dict={"result": result},
    )

    # print(result)

    # real_time_info = filter_subway_realtime_data(
    #     data=response_json,
    #     line_name=line_name,
    #     direction=direction,
    # )
    # return [real_time_info]
