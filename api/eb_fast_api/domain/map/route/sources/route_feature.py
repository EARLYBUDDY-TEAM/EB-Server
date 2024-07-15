import httpx
from eb_fast_api.env.env import settings
from eb_fast_api.domain.map.route.sources import route_schema


'''
{
	"error": {
		"msg": "출, 도착지가 700m이내입니다.",
		"code": "-98"
	}
}
'''
async def getRouteData(sx: float, sy: float, ex: float, ey: float) -> route_schema.Route:
    url = 'https://api.odsay.com/v1/api/searchPubTransPathT'
    params = {
        'apiKey': settings.odsay,
        'SX': sx,
        'SY': sy,
        'EX': ex,
        'EY': ey,
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