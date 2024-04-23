from pydantic import BaseModel

class DefaultResponse(BaseModel):
    isSuccess: bool