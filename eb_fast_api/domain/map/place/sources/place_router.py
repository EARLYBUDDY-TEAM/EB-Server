from fastapi import APIRouter, HTTPException
from eb_fast_api.domain.map.place.sources import place_feature


router = APIRouter(prefix="/map/place")


@router.get("/search")
async def searchPlace(
    query: str,
    x: str,
    y: str,
):
    response = await place_feature.getPlaceData(query, x, y)
    if 200 <= response.status_code < 300:
        return response.json()
    elif 400 <= response.status_code < 500:
        raise HTTPException(
            status_code=400,
            detail="잘못된 쿼리 요청",
        )
    else:
        raise HTTPException(
            status_code=500,
            detail="서버 에러",
        )