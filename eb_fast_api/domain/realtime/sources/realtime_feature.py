from eb_fast_api.service.realtime.sources import bus_realtime_service as bas
from eb_fast_api.service.realtime.sources import subway_realtime_service as sas


async def get_bus_station_realtime_json(
    station_id: int,
) -> dict:
    response = await bas.get_bus_station_realtime_info(station_id=station_id)
    return response.json()


async def get_seoul_subway_realtime_json(
    station_name: str,
) -> dict:
    response = await sas.get_seoul_subway_realtime_info(
        station_name=station_name,
    )
    return response.json()
