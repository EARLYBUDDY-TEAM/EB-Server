from pydantic import BaseModel
from typing import List, Optional, Self
from eb_fast_api.database.sources.model.models import Path
from eb_fast_api.snippets.sources import dictionary


class StationInfo(BaseModel):
    name: str

    @classmethod
    def fromJson(cls, j: dict):
        return StationInfo(name=j["stationName"])

    @classmethod
    def mock(cls) -> Self:
        return StationInfo(name="수서역")


class TransportInfo(BaseModel):
    subwayType: Optional[str] = None
    busNumber: Optional[str] = None
    busType: Optional[str] = None

    @classmethod
    def fromJson(cls, j: dict):
        subwayCode = dictionary.safeDict(["subwayCode"], j)
        subwayType = dictionary.safeDict([subwayCode], subwayCodeToType)
        busNumber = dictionary.safeDict(["busNo"], j)
        busCode = dictionary.safeDict(["type"], j)
        busType = dictionary.safeDict([busCode], busCodeToType)

        trans = TransportInfo(
            subwayType=subwayType,
            busNumber=busNumber,
            busType=busType,
        )
        return trans

    @classmethod
    def mockBus(cls) -> Self:
        return TransportInfo(
            subwayType=None,
            busNumer="1000",
            busType="일반",
        )

    @classmethod
    def mockSubway(cls) -> Self:
        return TransportInfo(
            subwayType="1호선",
            busNumer=None,
            busType=None,
        )


class SubPathInfo(BaseModel):
    type: int
    time: int
    startName: str
    startX: Optional[str]
    startY: Optional[str]
    endName: str
    distance: int
    transports: Optional[List[TransportInfo]]
    stations: Optional[List[StationInfo]]

    @classmethod
    def fromJson(cls, j: dict):
        tmpTrans = dictionary.safeDict(["lane"], j)
        transports = (
            list(map(TransportInfo.fromJson, tmpTrans)) if tmpTrans != None else None
        )
        tmpStations = dictionary.safeDict(["passStopList", "stations"], j)
        stations = (
            list(map(StationInfo.fromJson, tmpStations))
            if tmpStations != None
            else None
        )

        subPath = SubPathInfo(
            type=j["trafficType"],
            time=j["sectionTime"],
            startName=dictionary.safeDict(["startName"], j) or "",
            startX=str(dictionary.safeDict(["startX"], j)),
            startY=str(dictionary.safeDict(["startY"], j)),
            endName=dictionary.safeDict(["endName"], j) or "",
            distance=int(j["distance"]),
            transports=transports,
            stations=stations,
        )
        return subPath

    @classmethod
    def mock(cls) -> Self:
        return SubPathInfo(
            type=2,
            time=10,
            startName="수서역",
            startX="123.12",
            startY="123.12",
            endName="수서역",
            distance=10,
            transports=[
                TransportInfo.mockBus(),
                TransportInfo.mockSubway(),
                TransportInfo.mockBus(),
                TransportInfo.mockSubway(),
            ],
            stations=[
                StationInfo.mock(),
                StationInfo.mock(),
            ],
        )


class PathInfo(BaseModel):
    type: int
    time: int
    walkTime: int = 0
    payment: int
    busTransitCount: int
    subwayTransitCount: int
    subPaths: List[SubPathInfo]

    @classmethod
    def fromJson(cls, j: dict):
        info = j["info"]
        subPaths = list(map(SubPathInfo.fromJson, j["subPath"]))
        path = PathInfo(
            type=j["pathType"],
            time=info["totalTime"],
            payment=info["payment"],
            busTransitCount=info["busTransitCount"],
            subwayTransitCount=info["subwayTransitCount"],
            subPaths=subPaths,
        )
        return path

    @classmethod
    def mock(cls) -> Self:
        return PathInfo(
            type=2,
            time=10,
            walkTime=10,
            payment=1000,
            busTransitCount=10,
            subwayTransitCount=10,
            subPaths=[
                SubPathInfo.mock(),
                SubPathInfo.mock(),
                SubPathInfo.mock(),
            ],
        )

    def to_path(self, id: str) -> Path:
        data = self.model_dump(mode="json")
        return Path(
            id=id,
            data=data,
        )


class RouteInfo(BaseModel):
    type: int
    paths: List[PathInfo]

    @classmethod
    def fromJson(cls, j: dict):
        paths = list(map(PathInfo.fromJson, j["path"]))
        route = RouteInfo(type=j["searchType"], paths=paths)
        return route


busCodeToType = {
    1: "일반",
    2: "좌석",
    3: "마을버스",
    4: "직행좌석",
    5: "공항버스",
    6: "간선급행",
    10: "외곽",
    11: "간선",
    12: "지선",
    13: "순환",
    14: "광역",
    15: "급행",
    16: "관광버스",
    20: "농어촌버스",
    22: "경기도시외형버스",
    26: "급행간선",
}


subwayCodeToType = {
    1: "1호선",
    2: "2호선",
    3: "3호선",
    4: "4호선",
    5: "5호선",
    6: "6호선",
    7: "7호선",
    8: "8호선",
    9: "9호선",
    21: "인천1호선",
    22: "인천2호선",
    91: "GTX-A",
    101: "공항철도",
    102: "자기부상철도",
    104: "경의중앙선",
    107: "에버라인",
    108: "경춘선",
    109: "신분당선",
    110: "의정부경전철",
    112: "경강선",
    113: "우이신설선",
    114: "서해선",
    115: "김포골드라인",
    116: "수인분당선",
    117: "신림선",
}


"""

{
    "busNo": "서울01(출근.평일운행)",
    "type": 14,
    "busID": 2824016,
    "busLocalBlID": "107000006",
    "busCityCode": 1000,
    "busProviderCode": 4
}

가까운거리일때 예외처리

"""
