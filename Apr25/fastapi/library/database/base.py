"""database 
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
import datetime
from database.common import TransactionType

DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)





class Base(DeclarativeBase):
    """This is base for all models
    """


class Book(Base):
    """Books Model
    """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    quantity = Column(Integer)


class Librarian(Base):
    """Librarians
    """
    __tablename__ = "librarians"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    librarian_id = Column(Integer, ForeignKey("librarians.id"))
    borrower_name = Column(String)
    transaction_type = Column(Enum(TransactionType))
    date = Column(DateTime, default=datetime.datetime.utcnow)

    book = relationship("Book")
    librarian = relationship("Librarian")


Base.metadata.create_all(bind=engine)
