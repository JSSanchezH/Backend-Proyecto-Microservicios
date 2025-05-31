# app/middlewares/api_key_auth.py

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse

PUBLIC_PATHS = [
    "/api/continents",
    "/api/countries",
    "/api/states",
    "/api/cities",
    "/api/companies",
    "/api/UserCompany",
    "/api/absence_types",
    "/api/payment-methods",
    "/api/roles",
    "/api/auth",
    "/api/docs",
    "/api/redocs",
    "/api/openapi.json",
]


class ApiKeyAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, user_company_repo):
        super().__init__(app)
        self.user_company_repo = user_company_repo

    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if request.method == "OPTIONS" or any(path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        api_key = request.headers.get("X-API-KEY")
        if not api_key:
            return JSONResponse(
                status_code=401, content={"detail": "API key is missing"}
            )

        user_company = self.user_company_repo.find_by_api_key(api_key)
        if not user_company:
            return JSONResponse(status_code=401, content={"detail": "Invalid API key"})

        request.state.authenticated_user = user_company
        return await call_next(request)
