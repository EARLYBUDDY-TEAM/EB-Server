# from pydantic import BaseModel
# from typing import List, Optional, Self

# def getDataFromJson(k: str, j: dict) -> Optional[any]:
#     try:
#         return j[k]
#     except:
#         return None
    
# class Lane(BaseModel):
#     subwayName: Optional[str] = None
#     busName: Optional[str] = None

#     @classmethod
#     def fromJson(cls, j: dict) -> Self:
#         subwayName = getDataFromJson('name', j)
#         busName = getDataFromJson('busNo', j)
#         lane = Lane(
#             subwayName = subwayName,
#             busName = busName
#             )
#         return lane


# class SubPath(BaseModel):
#     trafficType: int
#     sectionTime: int
#     lanes: Optional[List[Lane]]

#     @classmethod
#     def fromJson(cls, j: dict) -> Self:
#         tmpLanes = getDataFromJson('lane', j)
#         lanes = list(map(Lane.fromJson, tmpLanes)) if tmpLanes != None else None
#         subPath = SubPath(
#             trafficType = j['trafficType'],
#             sectionTime = j['sectionTime'],
#             lanes = lanes
#         )
#         return subPath


# class PathInfo(BaseModel):
#     totalTime: int
#     totalWalkTime: int = 0
#     payment: int
#     busTransitCount: int
#     subwayTransitCount: int


# class Path(BaseModel):
#     pathType: int
#     info: PathInfo
#     subPaths: List[SubPath]

#     @classmethod
#     def fromJson(cls, j: dict) -> Self:
#         info = PathInfo.model_validate(j['info'])
#         subPaths = list(map(SubPath.fromJson, j['subPath']))
#         path = Path(
#             pathType = j['pathType'],
#             info = info,
#             subPaths = subPaths
#         )
#         return path


# class Route(BaseModel):
#     searchType: int
#     paths: List[Path]

#     @classmethod
#     def fromJson(cls, j: dict) -> Self:
#         paths = list(map(Path.fromJson, j['path']))
#         route = Route(
#             searchType = j['searchType'],
#             paths = paths
#         )
#         return route

from pydantic import BaseModel
from typing import List, Optional, Self
from eb_fast_api.snippets import snippets
    
class Transportation(BaseModel):
    subwayName: Optional[str] = None
    busName: Optional[str] = None

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        subwayName = snippets.getDataFromJson('name', j)
        busName = snippets.getDataFromJson('busNo', j)
        trans = Transportation(
            subwayName = subwayName,
            busName = busName
            )
        return trans

class SubPath(BaseModel):
    type: int
    time: int
    transportations: Optional[List[Transportation]]

    @classmethod
    def fromJson(cls, j: dict) -> Self:
        tmpTrans = snippets.getDataFromJson('lane', j)
        transportations = list(map(Transportation.fromJson, tmpTrans)) if tmpTrans != None else None
        subPath = SubPath(
            type = j['trafficType'],
            time = j['sectionTime'],
            transportations = transportations
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