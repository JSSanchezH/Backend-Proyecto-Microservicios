from pydantic import BaseModel, EmailStr
from typing import Optional


# Base para creación y actualización
class CompanyBase(BaseModel):
    name: str
    nit: int
    address: str
    email: EmailStr
    typeIndustry: str
    urlLogo: Optional[str] = None


# Para crear
class CompanyCreate(CompanyBase):
    pass


# Para actualizar
class CompanyUpdate(CompanyBase):
    pass


# Para respuestas
class CompanyRead(CompanyBase):
    company_id: int

    class Config:
        orm_mode = True
