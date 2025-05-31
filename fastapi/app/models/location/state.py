from app.db.database import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class State(Base):
    __tablename__ = "state"

    state_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    country_id = Column(Integer, ForeignKey("country.country_id"))

    country = relationship("Country", back_populates="states")
    cities = relationship("City", back_populates="state")
