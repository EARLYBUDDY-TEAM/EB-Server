from pydantic import BaseModel
from typing import List, Optional, Self
from eb_fast_api.snippets import snippets
    
class Transport(BaseModel):
    subwayName: Optional[str] = None
    busName: Optional[str] = None

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        subwayName = snippets.getDataFromJson('name', j)
        busName = snippets.getDataFromJson('busNo', j)
        trans = Transport(
            subwayName = subwayName,
            busName = busName
            )
        return trans

class SubPath(BaseModel):
    type: int
    time: int
    transports: Optional[List[Transport]]

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        tmpTrans = snippets.getDataFromJson('lane', j)
        transports = list(map(Transport.fromJson, tmpTrans)) if tmpTrans != None else None
        subPath = SubPath(
            type = j['trafficType'],
            time = j['sectionTime'],
            transports = transports
        )
        return subPath
    
class Path(BaseModel):
    type: int
    time: int
    walkTime: int = 0
    payment: int
    busTransitCount: int
    subwayTransitCount: int
    subPaths: List[SubPath]

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        info = j['info']
        subPaths = list(map(SubPath.fromJson, j['subPath']))
        path = Path(
            type = j['pathType'],
            time = info['totalTime'],
            payment = info['payment'],
            busTransitCount = info['busTransitCount'],
            subwayTransitCount = info['subwayTransitCount'],
            subPaths = subPaths
        )
        return path


class Route(BaseModel):
    type: int
    paths: List[Path]

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        paths = list(map(Path.fromJson, j['path']))
        route = Route(
            type = j['searchType'],
            paths = paths
        )
        return route