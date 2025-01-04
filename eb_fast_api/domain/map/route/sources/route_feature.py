from httpx import AsyncClient, Response
from typing import List
from eb_fast_api.env.sources.env import ENV_API
from eb_fast_api.domain.schema.sources.schemas import (
    SubPathInfo,
    PathInfo,
    RouteInfo,
)


def calTotalWalkTime(path: PathInfo):
    walkTime = sum([subPath.time for subPath in path.subPaths if subPath.type == 3])
    path.walkTime = walkTime


# walk subpath 중복이면 빈값처리 ...
def modifyWalkSubPath(
    subPaths: List[SubPathInfo],
    startPlace: str,
    endPlace: str,
):
    if not subPaths:
        return
    elif len(subPaths) == 1 and subPaths[0].type == 3:
        subPaths[0].startName = startPlace
        subPaths[0].endName = endPlace
        return
    else:
        for index, subPath in enumerate(subPaths):
            if subPath.type != 3:
                continue
            if index == 0:
                subPath.startName = startPlace
                subPath.endName = subPaths[index + 1].startName
            elif index == len(subPaths) - 1:
                subPath.startName = subPaths[index - 1].endName
                subPath.endName = endPlace
            else:
                subPath.startName = subPaths[index - 1].endName
                subPath.endName = subPaths[index + 1].startName


def refactorRoute(
    route: RouteInfo,
    startPlace: str,
    endPlace: str,
) -> RouteInfo:
    for path in route.paths:
        calTotalWalkTime(path)
        modifyWalkSubPath(path.subPaths, startPlace, endPlace)
    return route


async def getRouteData(
    sx: float,
    sy: float,
    ex: float,
    ey: float,
) -> Response:
    url = "https://api.odsay.com/v1/api/searchPubTransPathT"
    params = {
        "apiKey": ENV_API.odsay,
        "SX": sx,
        "SY": sy,
        "EX": ex,
        "EY": ey,
        "OPT": 0,
    }
    async with AsyncClient() as client:
        response = await client.get(url=url, params=params)
        return response


"""
{
	"error": {
		"msg": "출, 도착지가 700m이내입니다.",
		"code": "-98"
	}
}
"""
