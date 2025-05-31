from app.db.database import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    continent_id = Column(Integer, ForeignKey("continent.continent_id"))

    continent = relationship("Continent", back_populates="countries")
    states = relationship("State", back_populates="country")
