from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.state_schema import StateCreate, StateResponse, StateBatchCreate
from app.services.state_service import StateService
from app.db.session import get_db

router = APIRouter(prefix="/states", tags=["States"])


@router.get("/", response_model=List[StateResponse])
def get_all_states(db: Session = Depends(get_db)):
    return StateService(db).get_all()


@router.get("/{state_id}", response_model=StateResponse)
def get_state_by_id(state_id: int, db: Session = Depends(get_db)):
    state = StateService(db).get_by_id(state_id)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    return state


@router.post("/", response_model=StateResponse)
def create_state(state: StateCreate, db: Session = Depends(get_db)):
    return StateService(db).create(state)


@router.post("/batch", response_model=List[StateResponse])
def create_states_batch(batch: StateBatchCreate, db: Session = Depends(get_db)):
    return StateService(db).create_batch(batch.states)


@router.delete("/{state_id}", status_code=204)
def delete_state(state_id: int, db: Session = Depends(get_db)):
    state = StateService(db).delete(state_id)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
