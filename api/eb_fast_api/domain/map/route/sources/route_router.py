from fastapi import APIRouter
from eb_fast_api.domain.map.route.sources import route_feature
from eb_fast_api.domain.map.route.sources.route_schema import Coordi

router = APIRouter(prefix='/map/route')

@router.get('/find')
async def find_route(sx: float, sy: float, ex: float, ey: float):
    response = await route_feature.getRouteData(sx, sy, ex, ey)
    return response