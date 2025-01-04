from pydantic import BaseModel
from typing import Self


class CoordiInfo(BaseModel):
    x: str
    y: str

    @classmethod
    def mock(cls) -> Self:
        return CoordiInfo(
            x="127.10297988971773",
            y="37.48800665367514",
        )
