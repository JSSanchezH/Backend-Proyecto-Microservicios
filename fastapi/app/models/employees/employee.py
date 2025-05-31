from app.db.database import Base

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone_number = Column(Integer)
    hire_date = Column(Date)
    role_id = Column(Integer, ForeignKey("role.role_id"))
    manager_id = Column(Integer, ForeignKey("employee.employee_id"), nullable=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    url_foto = Column(String(100))
    status = Column(Boolean)

    role = relationship("Role", back_populates="employees")
    schedules = relationship("Schedule", back_populates="employee")
