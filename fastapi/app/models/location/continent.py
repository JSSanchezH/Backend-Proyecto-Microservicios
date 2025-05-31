from app.db.database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Continent(Base):
    __tablename__ = "continent"

    continent_id = Column(Integer, primary_key=True)
    name = Column(String(100))

    countries = relationship("Country", back_populates="continent")
