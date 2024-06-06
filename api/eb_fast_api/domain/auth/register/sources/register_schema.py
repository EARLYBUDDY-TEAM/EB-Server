from pydantic import BaseModel

class RegisterInfo(BaseModel):
    email: str
    password: str