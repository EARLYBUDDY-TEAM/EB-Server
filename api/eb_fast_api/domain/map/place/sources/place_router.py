from fastapi import APIRouter
from eb_fast_api.domain.map.place.sources import place_feature

router = APIRouter(prefix="/map/place")

@router.get("/search")
async def search_place(query: str, x: str, y: str):
    response = await place_feature.getPlaceData(query=query, x=x, y=y)
    return response