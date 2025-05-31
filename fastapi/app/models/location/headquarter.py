from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from app.db.database import Base


class Headquarter(Base):
    __tablename__ = "headquarters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    address = Column(String(50))
    phone = Column(BigInteger, nullable=False)

    city_id = Column(Integer, ForeignKey("city.city_id"), nullable=False)
    company_id = Column(Integer, ForeignKey("company.company_id"), nullable=False)

    city = relationship("City", back_populates="headquarters")
    company = relationship("Company", back_populates="headquarters")

    departments = relationship("Department", back_populates="headquarter")
