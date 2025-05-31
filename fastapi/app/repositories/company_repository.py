from sqlalchemy.orm import Session
from app.models.company.company import Company
from app.schemas.company_schema import CompanyCreate, CompanyUpdate


def get_all(db: Session):
    return db.query(Company).all()


def get_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.company_id == company_id).first()


def create(db: Session, company: CompanyCreate):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update(db: Session, company_id: int, company_data: CompanyUpdate):
    company = get_by_id(db, company_id)
    if not company:
        return None
    for field, value in company_data.dict().items():
        setattr(company, field, value)
    db.commit()
    db.refresh(company)
    return company


def delete(db: Session, company_id: int):
    company = get_by_id(db, company_id)
    if not company:
        return None
    db.delete(company)
    db.commit()
    return company
