from app.models.company.userCompany import UserCompany
from sqlalchemy.orm import Session


class UserCompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_api_key(self, api_key: str):
        return self.db.query(UserCompany).filter(UserCompany.api_key == api_key).first()
