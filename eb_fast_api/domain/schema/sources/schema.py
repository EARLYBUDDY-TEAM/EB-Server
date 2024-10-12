from pydantic import BaseModel
from typing import Optional, Self
from datetime import datetime
from eb_fast_api.database.sources.model.models import User, Schedule, Place
from eb_fast_api.snippets.sources import pwdcrypt


class Coordi(BaseModel):
    x: str
    y: str

    @classmethod
    def mock(cls):
        return Coordi(
            x="127.10297988971773",
            y="37.48800665367514",
        )


class PlaceInfo(BaseModel):
    id: str
    name: str
    address: str
    category: str
    distance: str
    coordi: Coordi

    @classmethod
    def fromPlace(cls, place: Place) -> Self:
        placeDict = place.__dict__

        return PlaceInfo(
            id=placeDict["id"],
            name=placeDict["name"],
            address=placeDict["address"],
            category=placeDict["category"],
            distance=placeDict["distance"],
            coordi=Coordi(
                x=placeDict["coordiX"],
                y=placeDict["coordiY"],
            ),
        )

    def toPlace(self) -> Place:
        return Place(
            id=self.id,
            name=self.name,
            address=self.address,
            category=self.category,
            distance=self.distance,
            coordiX=self.coordi.x,
            coordiY=self.coordi.y,
        )

    @classmethod
    def mock(cls):
        return PlaceInfo(
            id="id",
            name="name",
            address="address",
            category="category",
            distance="distance",
            coordi=Coordi.mock(),
        )


class LoginInfo(BaseModel):
    email: str
    password: str


class RegisterInfo(BaseModel):
    nickName: str
    email: str
    password: str

    def toUser(self, refreshToken: str) -> User:
        return User(
            email=self.email,
            nickName=self.nickName,
            hashedPassword=pwdcrypt.hash(self.password),
            refreshToken=refreshToken,
        )


class ScheduleInfo(BaseModel):
    id: Optional[int]
    title: str
    memo: Optional[str]
    time: datetime
    isNotify: bool
    startPlaceInfo: Optional[PlaceInfo]
    endPlaceInfo: Optional[PlaceInfo]

    def toSchedule(self) -> Schedule:
        startPlaceID = self.startPlaceInfo.id if self.startPlaceInfo != None else None
        endPlaceID = self.endPlaceInfo.id if self.endPlaceInfo != None else None

        return Schedule(
            title=self.title,
            memo=self.memo,
            time=self.time,
            isNotify=self.isNotify,
            startPlaceID=startPlaceID,
            endPlaceID=endPlaceID,
        )

    @classmethod
    def mock(cls):
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        startPlaceInfo = PlaceInfo.mock()
        startPlaceInfo.id = "startPlaceID"
        endPlaceInfo = PlaceInfo.mock()
        endPlaceInfo.id = "endPlaceID"

        return ScheduleInfo(
            id=None,
            title="title",
            memo="memo",
            time=time,
            isNotify=False,
            startPlaceInfo=startPlaceInfo,
            endPlaceInfo=endPlaceInfo,
        )

    @classmethod
    def mockWithID(cls):
        id = 10
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        startPlaceInfo = PlaceInfo.mock()
        startPlaceInfo.id = "startPlaceID"
        endPlaceInfo = PlaceInfo.mock()
        endPlaceInfo.id = "endPlaceID"

        return ScheduleInfo(
            id=id,
            title="title",
            memo="memo",
            time=time,
            isNotify=False,
            startPlaceInfo=startPlaceInfo,
            endPlaceInfo=endPlaceInfo,
        )


class Token(BaseModel):
    accessToken: str
    refreshToken: str
