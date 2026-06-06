from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URI = "sqlite:///storesdb.db"

engine = create_engine(
    DATABASE_URI,
    echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)



class Base(DeclarativeBase):
    pass