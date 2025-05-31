from app.repositories.state_repository import StateRepository
from app.models.location.state import State
from app.schemas.state_schema import StateCreate
from sqlalchemy.orm import Session
from typing import List


class StateService:
    def __init__(self, db: Session):
        self.repository = StateRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, state_id: int):
        return self.repository.get_by_id(state_id)

    def create(self, state_create: StateCreate):
        state = State(**state_create.dict())
        return self.repository.create(state)

    def create_batch(self, states_create: List[StateCreate]):
        states = [State(**s.dict()) for s in states_create]
        return self.repository.create_batch(states)

    def delete(self, state_id: int):
        return self.repository.delete(state_id)
