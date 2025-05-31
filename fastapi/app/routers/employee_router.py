from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import EmployeeService
from typing import List

router = APIRouter(tags=["Employees"])


@router.get("/", response_model=List[EmployeeResponse])
def list_employees(request: Request, db: Session = Depends(get_db)):
    return EmployeeService(db).list_employees()


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = EmployeeService(db).get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeService(db).create_employee(employee)


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int, data: EmployeeUpdate, db: Session = Depends(get_db)
):
    updated = EmployeeService(db).update_employee(employee_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@router.delete("/{employee_id}", response_model=EmployeeResponse)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted = EmployeeService(db).delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted
