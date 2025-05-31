from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.role_service import RoleService
from app.schemas.role_schema import RoleCreate, RoleOut

router = APIRouter(tags=["Roles"])


@router.get("/", response_model=list[RoleOut])
def list_roles(db: Session = Depends(get_db)):
    return RoleService(db).get_all()


@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = RoleService(db).get_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/", response_model=RoleOut, status_code=status.HTTP_201_CREATED)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return RoleService(db).create(role)


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    if not RoleService(db).delete(role_id):
        raise HTTPException(status_code=404, detail="Role not found")
