from httpx import AsyncClient, Response
from eb_fast_api.env.sources.env import ENV_API


async def get_seoul_subway_realtime_json(
    station_name: str,
) -> Response:
    apiKey = ENV_API.seoul_subway
    url = f"http://swopenAPI.seoul.go.kr/api/subway/{apiKey}/json/realtimeStationArrival/0/30/{station_name}"
    async with AsyncClient() as client:
        response = await client.get(url=url)
        return response
