from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyRead
from app.services import company_service as service

from app.db.session import get_db


router = APIRouter(tags=["Company"])


@router.get("/", response_model=list[CompanyRead])
def get_companies(db: Session = Depends(get_db)):
    return service.get_all_companies(db)


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = service.get_company_by_id(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.post("/", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return service.create_company(db, company)


@router.put("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)
):
    updated = service.update_company(db, company_id, company)
    if not updated:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated


@router.delete("/{company_id}", response_model=CompanyRead)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_company(db, company_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Company not found")
    return deleted
