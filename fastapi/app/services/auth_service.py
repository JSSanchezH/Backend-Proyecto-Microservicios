from sqlalchemy.orm import Session
from app.models.company.company import Company
from app.models.company.userCompany import UserCompany
from app.schemas.auth_schema import (
    CompanyRegisterRequest,
    CompanyLoginRequest,
    LoginResponse,
)
from app.security import hash_password, verify_password, generate_api_key
from fastapi import HTTPException, status


def register_company_with_user(db: Session, request: CompanyRegisterRequest):
    existing_user = (
        db.query(UserCompany)
        .filter(UserCompany.userName == request.user.userName)
        .first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    company = Company(
        name=request.company.name,
        nit=request.company.nit,
        address=request.company.address,
        email=request.company.email,
        typeIndustry=request.company.typeIndustry,
        urlLogo=request.company.urlLogo,
    )
    db.add(company)
    db.commit()
    db.refresh(company)

    user = UserCompany(
        userName=request.user.userName,
        password=hash_password(request.user.password),
        api_key=generate_api_key(),
        company_id=company.company_id,
    )
    db.add(user)
    db.commit()

    return "Company and user registered successfully"


def login(db: Session, request: CompanyLoginRequest) -> LoginResponse:
    user = (
        db.query(UserCompany).filter(UserCompany.userName == request.userName).first()
    )
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    return LoginResponse(api_key=user.api_key, company_id=user.company_id)
