from eb_fast_api.service.realtime.sources.service.subway_realtime_service import (
    subway_realtime_service as srs,
)
from eb_fast_api.snippets.sources import eb_datetime
import asyncio
from eb_fast_api.service.realtime.check import json_helper as jh


if __name__ == "__main__":
    station_name = "논현"
    line_name = "7호선"
    up_or_down = 0

    realtime_info = asyncio.run(
        srs.request(
            station_name=station_name,
            line_name=line_name,
            up_or_down=up_or_down,
        )
    )
