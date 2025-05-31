from sqlalchemy.orm import Session
from app.repositories import company_repository as repo
from app.schemas.company_schema import CompanyCreate, CompanyUpdate


def get_all_companies(db: Session):
    return repo.get_all(db)


def get_company_by_id(db: Session, company_id: int):
    return repo.get_by_id(db, company_id)


def create_company(db: Session, company_data: CompanyCreate):
    return repo.create(db, company_data)


def update_company(db: Session, company_id: int, company_data: CompanyUpdate):
    return repo.update(db, company_id, company_data)


def delete_company(db: Session, company_id: int):
    return repo.delete(db, company_id)
