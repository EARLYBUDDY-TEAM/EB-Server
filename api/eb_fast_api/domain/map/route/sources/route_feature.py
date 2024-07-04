import httpx
from eb_fast_api.env.env import settings
from eb_fast_api.domain.map.route.sources import route_schema

async def getRouteData() -> route_schema.Route:
    url = 'https://api.odsay.com/v1/api/searchPubTransPathT'
    params = {
        'apiKey': settings.odsay,
        'SX': 127.10297988971773,
        'SY': 37.48800665367514,
        'EX': 126.994596,
        'EY': 37.534542,
        'OPT': 0
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, params=params)
        responseJson = response.json()['result']
        route = route_schema.Route.fromJson(responseJson)
        for path in route.paths:
            calTotalWalkTime(path)
        return route

def calTotalWalkTime(path: route_schema.Path):
    walkTime = sum([
        subPath.time
        for subPath in path.subPaths 
        if subPath.type == 3
    ])
    path.walkTime = walkTime