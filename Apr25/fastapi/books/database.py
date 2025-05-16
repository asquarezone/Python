"""This module contains necessary classes and methods for persistence
"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    """The Base class maintains catalog of classes and tables
    """


class Book(Base):
    """This represents the books table
    """
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]

DATABASE_URL = "sqlite:///.test.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

