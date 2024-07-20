from fastapi import APIRouter
from eb_fast_api.domain.map.route.sources import route_feature

router = APIRouter(prefix='/map/route')

@router.get('/find')
async def find_route(sx: float, sy: float, ex: float, ey: float, startPlace: str, endPlace: str):
    response = await route_feature.getRouteData(sx, sy, ex, ey, startPlace, endPlace)
    return response