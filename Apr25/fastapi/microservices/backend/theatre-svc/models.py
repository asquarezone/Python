"""This module will have database models
"""

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Theatre(Base):
    """This represents the database table theatres
    """
    __tablename__ = "theatres"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(String(1000))
