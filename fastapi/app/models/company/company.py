from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class Company(Base):
    __tablename__ = "company"

    company_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nit = Column(Integer)
    address = Column(String(100))
    email = Column(String(50))
    typeIndustry = Column(String(30))
    urlLogo = Column(String(100))

    users = relationship("UserCompany", back_populates="company")
    headquarters = relationship("Headquarter", back_populates="company")
