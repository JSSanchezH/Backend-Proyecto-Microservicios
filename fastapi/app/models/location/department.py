from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    headquarter_id = Column(Integer, ForeignKey("headquarters.id"), nullable=False)
    headquarter = relationship("Headquarter", back_populates="departments")
