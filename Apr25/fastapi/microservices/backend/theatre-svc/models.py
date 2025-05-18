"""This module will have database models
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Theatre(Base):
    """This represents the database table theatres
    """
    __tablename__ = "theatres"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(String(1000))
    screens = relationship("Screen", back_populates="theatre", cascade="all, delete")


class Screen(Base):
    """This class represents the database table screens
    """
    __tablename__ = "screens"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), nullable=False)
    theatre_id = Column(Integer, ForeignKey("theatres.id"))
    theatre = relationship("Theatre", back_populates="screens")
