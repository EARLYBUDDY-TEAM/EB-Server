from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    subway_realtime_service as srs,
)
from eb_fast_api.snippets.sources import eb_datetime
from eb_fast_api.snippets.sources import dictionary
import json
import asyncio
from pathlib import Path
from eb_fast_api.service.realtime.sources.realtime_service_schema import ArrivalInfo


async def get_and_log_response(
    station_name: str,
    line_name: str,
    direction: int,
):
    parent_path = Path(__file__).resolve().parent
    now_time = eb_datetime.get_datetime_now()

    response = await srs.get_seoul_subway_realtime_info(station_name=station_name)
    response_json = response.json()
    realtime_json_list = srs.filter_subway_realtime_json(
        json=response_json,
        line_name=line_name,
        direction=direction,
    )

    dummy_file = f"{parent_path}/dummy.json"
    json_file_name = f"{station_name}_{now_time}.json"
    file_name = f"{parent_path}/{json_file_name}"
    dummy_dict = dict()
    with open(dummy_file, "r", encoding="utf-8-sig") as fp:
        dummy_dict = json.load(fp)

    for realtime_json in realtime_json_list:
        arvlMsg2 = dictionary.safeDict(
            keyList=["arvlMsg2"],
            fromDict=realtime_json,
        )
        arvlMsg3 = dictionary.safeDict(
            keyList=["arvlMsg3"],
            fromDict=realtime_json,
        )
        arvlCd = dictionary.safeDict(
            keyList=["arvlCd"],
            fromDict=realtime_json,
        )
        recptnDt = dictionary.safeDict(
            keyList=["recptnDt"],
            fromDict=realtime_json,
        )
        dummy_content = {
            "fileName": json_file_name,
            "arvlMsg2": arvlMsg2,
            "arvlMsg3": arvlMsg3,
            "arvlCd": arvlCd,
            "recptnDt": recptnDt,
        }
        dummy_dict.append(dummy_content)
        print(dummy_dict)

    with open(dummy_file, "w", encoding="utf-8-sig") as fp:
        json.dump(
            dummy_dict,
            fp,
            ensure_ascii=False,
        )

    arrival_info_list = srs.get_subway_arrival_info_list(
        filtered_realtime_json_list=realtime_json_list,
    )
    for arrival_info in arrival_info_list:
        arrival_info_dict = arrival_info.model_dump(mode="json")
        realtime_json_list.append(arrival_info_dict)

    with open(file_name, "w", encoding="UTF-8-sig") as fp:
        json.dump(
            realtime_json_list,
            fp,
            ensure_ascii=False,
        )

    # json.dump(response_json, fp)
    # real_time_info = srs.filter_subway_realtime_data(
    #     data=response_json,
    #     line_name=line_name,
    #     direction=direction,
    # )

    # return real_time_info


if __name__ == "__main__":
    station_name = "시청"
    line_name = "1호선"
    up_or_down = 0

    asyncio.run(
        srs.request(
            station_name=station_name,
            line_name=line_name,
            up_or_down=up_or_down,
        )
    )

    # asyncio.run(
    #     get_and_log_response(
    #         station_name=station_name,
    #         line_name=line_name,
    #         direction=direction,
    #     )
    # )
