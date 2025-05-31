from pydantic import BaseModel
from typing import List


class ContinentBase(BaseModel):
    name: str


class ContinentCreate(ContinentBase):
    pass


class ContinentOut(ContinentBase):
    continent_id: int

    class Config:
        orm_mode = True


class ContinentBatchCreate(BaseModel):
    continents: List[ContinentCreate]
