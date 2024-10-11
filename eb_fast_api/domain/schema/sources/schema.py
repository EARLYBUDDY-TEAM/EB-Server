from pydantic import BaseModel
from typing import Optional
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
    title: str
    memo: Optional[str] = None
    time: datetime
    isNotify: bool
    startPlaceID: Optional[str] = None
    endPlaceID: Optional[str] = None

    def toSchedule(self) -> Schedule:
        return Schedule(
            title=self.title,
            memo=self.memo,
            time=self.time,
            isNotify=self.isNotify,
            startPlaceID=self.startPlaceID,
            endPlaceID=self.endPlaceID,
        )

    @classmethod
    def mock(cls):
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)

        return ScheduleInfo(
            title="title",
            memo="memo",
            time=time,
            isNotify=False,
            startPlaceID="startPlace",
            endPlaceID="endPlace",
        )


class Token(BaseModel):
    accessToken: str
    refreshToken: str
