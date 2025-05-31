from pydantic import BaseModel
from typing import List


class CountryBase(BaseModel):
    name: str
    continent_id: int


class CountryCreate(CountryBase):
    pass


class CountryUpdate(CountryBase):
    pass


class CountryInDB(BaseModel):
    country_id: int
    name: str
    continent_id: int

    class Config:
        orm_mode = True


class CountryResponse(BaseModel):
    country_id: int
    name: str
    continent_id: int

    class Config:
        orm_mode = True


class CountryBatchCreate(BaseModel):
    countries: List[CountryCreate]
