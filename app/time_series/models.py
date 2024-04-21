from pydantic import Field
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base
from ..database import Base


class TimeSeries(Base):
    __tablename__ = 'time_series'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    variable = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    ingestion_time = Column(DateTime, nullable=False)
