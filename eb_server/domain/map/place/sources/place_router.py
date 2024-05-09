from fastapi import APIRouter
from starlette import status
import httpx
from eb_server.env.env import settings

router = APIRouter(prefix='/map/place')

async def getPlaceData(search_text: str):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    header = { 'Authorization' : f'KakaoAK {settings.kakao_rest_api_key}' }
    params = {'query' : search_text}
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=header, params=params)
        return response.json()

@router.get('/search')
async def search_place(search_text: str):
    response = await getPlaceData(search_text)
    return response