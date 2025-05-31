from app.db.database import Base

from sqlalchemy import Column, ForeignKey, Integer, Time
from sqlalchemy.orm import relationship


class Schedule(Base):
    __tablename__ = "schedule"

    schedule_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee.employee_id"))
    start_time = Column(Time)
    end_time = Column(Time)
    break_start = Column(Time)
    break_end = Column(Time)

    employee = relationship("Employee", back_populates="schedules")
