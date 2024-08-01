from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Coordi(BaseModel):
    x: str
    y: str

class PlaceInfo(BaseModel):
    id: str
    name: str
    address: str
    category: str
    distance: str
    coordi: Coordi

class ScheduleInfo(BaseModel):
    title: str
    memo: Optional[str] = None
    time: datetime
    isNotify: bool
    startPlace: Optional[PlaceInfo] = None
    endPlace: Optional[PlaceInfo] = None