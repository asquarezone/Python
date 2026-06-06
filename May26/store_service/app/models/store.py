from sqlalchemy import String, Integer
from sqlalchemy import Column
from app.db.base import Base


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    city = Column(String(50))
    area = Column(String(200))
    address = Column(String(200))
