from app.db.database import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class UserCompany(Base):
    __tablename__ = "user_company"

    user_company_id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("company.company_id"))
    userName = Column(String(50))
    password = Column(String(100))
    api_key = Column(String(255))

    company = relationship("Company", back_populates="users")
