from app.db.database import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    state_id = Column(Integer, ForeignKey("state.state_id"))

    state = relationship("State", back_populates="cities")
    headquarters = relationship("Headquarter", back_populates="city")
