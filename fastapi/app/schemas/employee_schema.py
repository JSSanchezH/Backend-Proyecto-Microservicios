from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class EmployeeBase(BaseModel):
    name: str
    lastname: str
    email: EmailStr
    phone: str
    role_id: int
    schedule_id: int
    department_id: int


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str]
    lastname: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    role_id: Optional[int]
    schedule_id: Optional[int]
    department_id: Optional[int]


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
