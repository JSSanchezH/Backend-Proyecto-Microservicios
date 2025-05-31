from app.models.location.state import State
from sqlalchemy.orm import Session
from typing import List


class StateRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[State]:
        return self.db.query(State).all()

    def get_by_id(self, state_id: int) -> State:
        return self.db.query(State).filter(State.state_id == state_id).first()

    def create(self, state: State):
        self.db.add(state)
        self.db.commit()
        self.db.refresh(state)
        return state

    def create_batch(self, states: List[State]):
        self.db.add_all(states)
        self.db.commit()
        return states

    def delete(self, state_id: int):
        state = self.get_by_id(state_id)
        if state:
            self.db.delete(state)
            self.db.commit()
        return state
