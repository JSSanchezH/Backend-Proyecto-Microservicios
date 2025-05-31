from sqlalchemy.orm import Session
from app.models.employees.role import Role
from app.schemas.role_schema import RoleCreate


class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        return self.db.query(Role).all()

    def find_by_id(self, role_id: int):
        return self.db.query(Role).filter(Role.role_id == role_id).first()

    def save(self, role_data: RoleCreate):
        role = Role(name=role_data.name)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete(self, role_id: int):
        role = self.find_by_id(role_id)
        if role:
            self.db.delete(role)
            self.db.commit()
        return role
