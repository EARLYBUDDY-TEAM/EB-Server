from fastapi import APIRouter, HTTPException
from eb_fast_api.domain.map.route.sources import route_feature
from eb_fast_api.domain.map.route.sources.route_schema import RouteInfo


router = APIRouter(prefix="/map/route")


@router.get("/find")
async def findRoute(
    sx: float, sy: float, ex: float, ey: float, startPlace: str, endPlace: str
):
    response = await route_feature.getRouteData(sx, sy, ex, ey)
    if 200 <= response.status_code < 300:
        responseJson = response.json()["result"]
        route = RouteInfo.fromJson(responseJson)
        route = route_feature.refactorRoute(route, startPlace, endPlace)
        return route
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
