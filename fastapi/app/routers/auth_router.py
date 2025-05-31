from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.auth_schema import (
    CompanyRegisterRequest,
    CompanyLoginRequest,
    LoginResponse,
)
from app.services import auth_service

router = APIRouter(tags=["Auth"])


@router.post("/register")
def register(request: CompanyRegisterRequest, db: Session = Depends(get_db)):
    return auth_service.register_company_with_user(db, request)


@router.post("/login", response_model=LoginResponse)
def login(request: CompanyLoginRequest, db: Session = Depends(get_db)):
    return auth_service.login(db, request)
