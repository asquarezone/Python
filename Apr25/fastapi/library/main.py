from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.base import SessionLocal, Book, Librarian, Transaction
from models.base import BookCreate, LibrarianCreate, TransactionCreate
from database.common import TransactionType

app = FastAPI(
    title="Library API",
    summary="Library for learning",
    description="FastAPI for Library",
    version="0.0.1"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@app.post("/books")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get("/librarians")
def get_librarians(db: Session = Depends(get_db)):
    return db.query(Librarian).all()


@app.post("/librarians")
def create_librarian(librarian: LibrarianCreate, db: Session = Depends(get_db)):
    new_librarian = Librarian(**librarian.model_dump())
    db.add(new_librarian)
    db.commit()
    db.refresh(new_librarian)
    return new_librarian


@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


@app.post("/transactions")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == transaction.book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    librarian = db.query(Librarian).filter(
        Librarian.id == transaction.librarian_id)
    if not librarian:
        raise HTTPException(status_code=404, detail="Librarian not found")

    if transaction.transaction_type == TransactionType.BORROW:
        book.quantity -= 1
    else:
        book.quantity += 1

    new_transaction = Transaction(**transaction.model_dump())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction
