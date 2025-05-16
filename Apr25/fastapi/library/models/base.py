from pydantic import BaseModel
from typing import List
from database.common import TransactionType
from datetime import datetime


class BookCreate(BaseModel):
    title: str
    author: str
    quantity: int

class LibrarianCreate(BaseModel):
    name: str
    email: str

class TransactionCreate(BaseModel):
    book_id: int
    librarian_id: int
    borrower_name: str
    transaction_type: TransactionType


class BookResponse(BookCreate):
    id: int

class LibrarianResponse(LibrarianCreate):
    id: int

class TransactionResponse(TransactionCreate):
    id: int
    date: datetime
    