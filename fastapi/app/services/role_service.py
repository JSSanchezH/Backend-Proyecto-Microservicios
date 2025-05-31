from sqlalchemy.orm import Session
from app.schemas.role_schema import RoleCreate
from app.repositories.role_repository import RoleRepository


class RoleService:
    def __init__(self, db: Session):
        self.repo = RoleRepository(db)

    def get_all(self):
        return self.repo.find_all()

    def get_by_id(self, role_id: int):
        return self.repo.find_by_id(role_id)

    def create(self, role_data: RoleCreate):
        return self.repo.save(role_data)

    def delete(self, role_id: int):
        return self.repo.delete(role_id)
