from fastapi import FastAPI
from app.middlewares.api_key_auth import ApiKeyAuthMiddleware
from app.repositories.user_company_repo import UserCompanyRepository
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import SessionLocal, engine

from app.models.company import (
    company as company_model,
    userCompany as userCompany_model,
)

from app.models.location import (
    continent as continent_model,
    country as country_model,
    state as state_model,
    city as city_model,
    headquarter as headquarter_model,
    department as department_model,
)

from app.models.employees import (
    employee as employee_model,
    role as role_model,
    schedule as schedule_model,
)

from app.routers import (
    company_router,
    auth_router,
    employee_router,
    role_router,
    continent_router,
    country_router,
)


models = [
    company_model,
    userCompany_model,
    continent_model,
    country_model,
    state_model,
    city_model,
    headquarter_model,
    department_model,
    employee_model,
    role_model,
    schedule_model,
]

for model in models:
    model.Base.metadata.create_all(bind=engine)


# FastAPI app
app = FastAPI(
    title="FastAPI Example",
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db = SessionLocal()
user_company_repo = UserCompanyRepository(db)

# API Key Middleware
app.add_middleware(ApiKeyAuthMiddleware, user_company_repo=user_company_repo)


routes = [
    (company_router.router, "/company"),
    (auth_router.router, "/auth"),
    (employee_router.router, "/employees"),
    (role_router.router, "/roles"),
    (continent_router.router, "/continents"),
    (country_router.router, "/countries"),
]

for router, prefix in routes:
    app.include_router(router, prefix=prefix)
