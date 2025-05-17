"""This module will have database models
"""

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Movie(Base):
    """This represents the database table movies
    """
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    language = Column(String(50))
    duration = Column(Float)
    rating = Column(Float)
