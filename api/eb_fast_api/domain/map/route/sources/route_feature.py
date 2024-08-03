import httpx
from eb_fast_api.env.env import ENV
from eb_fast_api.domain.map.route.sources import route_schema


async def getRouteData(
        sx: float,
        sy: float,
        ex: float,
        ey: float,
        startPlace: str, 
        endPlace: str,
    ) -> route_schema.Route:
    url = 'https://api.odsay.com/v1/api/searchPubTransPathT'
    params = {
        'apiKey': ENV.odsay,
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
            route_schema.calTotalWalkTime(path)
            route_schema.modifyWalkSubPath(path.subPaths, startPlace, endPlace)
        return route
    

'''
{
	"error": {
		"msg": "출, 도착지가 700m이내입니다.",
		"code": "-98"
	}
}
'''