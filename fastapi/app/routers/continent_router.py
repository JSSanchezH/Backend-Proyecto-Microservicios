from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.continent_schema import (
    ContinentCreate,
    ContinentOut,
    ContinentBatchCreate,
)
from app.services.continent_service import ContinentService

router = APIRouter(tags=["Continents"])


@router.get("/", response_model=list[ContinentOut])
def list_continents(db: Session = Depends(get_db)):
    return ContinentService(db).get_all()


@router.get("/{continent_id}", response_model=ContinentOut)
def get_continent(continent_id: int, db: Session = Depends(get_db)):
    continent = ContinentService(db).get_by_id(continent_id)
    if not continent:
        raise HTTPException(status_code=404, detail="Continent not found")
    return continent


@router.post("/", response_model=ContinentOut, status_code=status.HTTP_201_CREATED)
def create_continent(continent: ContinentCreate, db: Session = Depends(get_db)):
    return ContinentService(db).create(continent)


@router.post(
    "/batch", response_model=list[ContinentOut], status_code=status.HTTP_201_CREATED
)
def create_continent_batch(
    payload: ContinentBatchCreate, db: Session = Depends(get_db)
):
    return ContinentService(db).create_batch(payload.continents)


@router.delete("/{continent_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_continent(continent_id: int, db: Session = Depends(get_db)):
    if not ContinentService(db).delete(continent_id):
        raise HTTPException(status_code=404, detail="Continent not found")
