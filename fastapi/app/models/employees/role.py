from app.db.database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True)
    name = Column(String(50))

    employees = relationship("Employee", back_populates="role")
