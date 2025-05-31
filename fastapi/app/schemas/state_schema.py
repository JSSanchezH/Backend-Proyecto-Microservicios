from typing import List
from pydantic import BaseModel


class StateBase(BaseModel):
    name: str
    country_id: int


class StateCreate(StateBase):
    pass


class StateResponse(StateBase):
    state_id: int

    class Config:
        orm_mode = True


class StateBatchCreate(BaseModel):
    states: List[StateCreate]
