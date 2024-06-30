from pydantic import BaseModel
from typing import List

class SubPath(BaseModel):
    trafficType: int
    sectionTime: int

class PathInfo(BaseModel):
    totalTime: int
    totalWalkTime: int = 0
    payment: int
    busTransitCount: int
    subwayTransitCount: int

class Path(BaseModel):
    pathType: int
    info: PathInfo
    subPaths: List[SubPath]

    @classmethod
    def fromJson(cls, j: dict):
        info = PathInfo.model_validate(j['info'])
        subPaths = list(map(SubPath.model_validate, j['subPath']))
        path = Path(
            pathType = j['pathType'],
            info = info,
            subPaths = subPaths
        )
        return path

class Route(BaseModel):
    searchType: int
    paths: List[Path]

    @classmethod
    def fromJson(cls, j: dict):
        paths = list(map(Path.fromJson, j['path']))
        route = Route(
            searchType = j['searchType'],
            paths = paths
        )
        return route