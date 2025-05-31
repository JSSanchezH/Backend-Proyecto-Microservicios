from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class RoleOut(RoleBase):
    role_id: int

    class Config:
        orm_mode = True
