from sqlalchemy.orm import Session
from app.models.employees.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Employee).all()

    def get_by_id(self, employee_id: int):
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def create(self, employee_data: EmployeeCreate):
        employee = Employee(**employee_data.dict())
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def update(self, employee_id: int, data: EmployeeUpdate):
        employee = self.get_by_id(employee_id)
        if not employee:
            return None
        for key, value in data.dict(exclude_unset=True).items():
            setattr(employee, key, value)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete(self, employee_id: int):
        employee = self.get_by_id(employee_id)
        if not employee:
            return None
        self.db.delete(employee)
        self.db.commit()
        return employee
