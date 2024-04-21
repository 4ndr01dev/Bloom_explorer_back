from sqlalchemy import Column, Field, Integer, List, String, string
from sqlalchemy.orm import declarative_base

from ..database import Base

class Organizations(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    zone = Column(String, nullable=False)
    zone_id = Column(Integer, nullable=False)
    polygon_decoded = Column(String, nullable=False)
