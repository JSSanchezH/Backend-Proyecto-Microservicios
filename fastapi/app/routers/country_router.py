from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.country_service import CountryService
from app.schemas.country_schema import (
    CountryCreate,
    CountryUpdate,
    CountryBatchCreate,
    CountryResponse,
)
from typing import List

router = APIRouter(tags=["Countries"])


@router.get("/", response_model=List[CountryResponse])
def get_all(db: Session = Depends(get_db)):
    return CountryService(db).get_all()


@router.get("/{country_id}", response_model=CountryResponse)
def get_by_id(country_id: int, db: Session = Depends(get_db)):
    country = CountryService(db).get_by_id(country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@router.post("/", response_model=CountryResponse)
def create(country: CountryCreate, db: Session = Depends(get_db)):
    return CountryService(db).create(country)


@router.post("/batch", response_model=List[CountryResponse])
def create_batch(batch_data: CountryBatchCreate, db: Session = Depends(get_db)):
    return CountryService(db).create_batch(batch_data)


@router.put("/{country_id}", response_model=CountryResponse)
def update(country_id: int, country_data: CountryUpdate, db: Session = Depends(get_db)):
    country = CountryService(db).update(country_id, country_data)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@router.delete("/{country_id}", response_model=CountryResponse)
def delete(country_id: int, db: Session = Depends(get_db)):
    country = CountryService(db).delete(country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country
