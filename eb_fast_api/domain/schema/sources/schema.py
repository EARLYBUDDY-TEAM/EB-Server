from pydantic import BaseModel
from eb_fast_api.snippets.sources import pwdcrypt
from typing import Optional
from datetime import datetime
from eb_fast_api.database.sources.model.models import User, Schedule, Place


class Coordi(BaseModel):
    x: str
    y: str

    def __init__(self, x: str, y: str):
        super().__init__(x=x, y=y)

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


class ScheduleInfo(BaseModel):
    title: str
    time: datetime
    isNotify: bool
    memo: Optional[str] = None
    startPlace: Optional[PlaceInfo] = None
    endPlace: Optional[PlaceInfo] = None

    def toSchedule(self) -> Schedule:
        schedule = Schedule(
            title=self.title,
            time=self.time,
            isNotify=self.isNotify,
            memo=self.memo,
        )

        if self.startPlace != None:
            schedule.startPlaceID = self.startPlace.id

        if self.endPlace != None:
            schedule.endPlaceID = self.endPlace.id

        return schedule

    @classmethod
    def mock(cls):
        timeString = "2024-07-28T05:04:32.299Z"
        time = datetime.fromisoformat(timeString)
        startPlace = PlaceInfo.mock()
        startPlace.id = "startPlaceID"
        endPlace = PlaceInfo.mock()
        endPlace.id = "endPlaceID"

        return ScheduleInfo(
            title="title",
            memo="memo",
            time=time,
            isNotify=False,
            startPlace=startPlace,
            endPlace=endPlace,
        )


class UserInfo(BaseModel):
    email: str
    password: str

    def __init__(self, email: str, password: str):
        super().__init__(email=email, password=password)

    def toUser(self) -> User:
        return User(
            email=self.email,
            hashedPassword=pwdcrypt.hash(self.password),
        )


class Token(BaseModel):
    accessToken: str
    refreshToken: str

    def __init__(
        self,
        accessToken: str,
        refreshToken: str,
    ):
        super().__init__(
            accessToken=accessToken,
            refreshToken=refreshToken,
        )
