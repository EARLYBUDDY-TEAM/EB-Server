import httpx
from eb_fast_api.env.env import settings


async def getPlaceData(query: str, x: str, y: str):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    header = {"Authorization": f"KakaoAK {settings.kakaomap_local}"}
    params = {
        "query": query,
        "x": x,
        "y": y,
        "sort": "distance",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=header, params=params)
        return response.json()
 