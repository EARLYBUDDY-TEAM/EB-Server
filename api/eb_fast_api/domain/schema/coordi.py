from pydantic import BaseModel


class Coordi(BaseModel):
    x: str
    y: str

    def __init__(self, x: str, y: str):
        super().__init__(x = x, y = y)

    @classmethod
    def mock(cls):
        return Coordi(
            x="127.10297988971773",
            y="37.48800665367514",
        )