from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class UserCreate(BaseModel):
    email: str
    # email: str
    password: str

    # @field_validator('email', 'password')
    # def not_empty(cls, v):
    #     if not v or not v.strip():
    #         raise ValueError('빈 값은 허용되지 않습니다.')
    #     return v