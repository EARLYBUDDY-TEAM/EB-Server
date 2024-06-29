from pydantic import BaseModel
from typing import List

class PathInfo(BaseModel):
    totalTime: int
    payment: int
    busTransitCount: int
    subwayTransitCount: int

class Path(BaseModel):
    pathType: int
    info: PathInfo

    @classmethod
    def fromJson(cls, j: dict):
        info = PathInfo.model_validate(j['info'])
        path = Path(
            pathType = j['pathType'],
            info = info
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