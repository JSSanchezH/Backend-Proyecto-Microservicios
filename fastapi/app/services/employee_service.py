from sqlalchemy.orm import Session
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


class EmployeeService:
    def __init__(self, db: Session):
        self.repo = EmployeeRepository(db)

    def list_employees(self):
        return self.repo.get_all()

    def get_employee(self, employee_id: int):
        return self.repo.get_by_id(employee_id)

    def create_employee(self, data: EmployeeCreate):
        return self.repo.create(data)

    def update_employee(self, employee_id: int, data: EmployeeUpdate):
        return self.repo.update(employee_id, data)

    def delete_employee(self, employee_id: int):
        return self.repo.delete(employee_id)
