from pydantic import BaseModel, EmailStr


class CompanyBase(BaseModel):
    name: str
    nit: int
    address: str
    email: EmailStr
    typeIndustry: str
    urlLogo: str


class UserBase(BaseModel):
    userName: str
    password: str


class CompanyRegisterRequest(BaseModel):
    company: CompanyBase
    user: UserBase


class CompanyLoginRequest(BaseModel):
    userName: str
    password: str


class LoginResponse(BaseModel):
    api_key: str
    company_id: int
