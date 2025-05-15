from fastapi import FastAPI
from models import Book, BookResponse

app = FastAPI(
    title="BookStore",
    summary="Books store for learning",
    description="FastAPI for books store",
    version="0.0.1"
)

books: list[BookResponse] = []


@app.get("/books")
async def get_all_books() -> list[BookResponse]:
    """Gets all the books

    Returns:
        list[BookResponse]: all books
    """
    return books


@app.get("/books/{book_id}")
async def get_book(book_id: int) -> BookResponse | None:
    """Get a specific book
    """
    book = [book for book in books if book.book_id == book_id]
    return book


@app.post("/books")
async def create_book(book: Book) -> BookResponse:
    """Create a book
    """
    response = BookResponse(book_id=len(
        books)+1, title=book.title, author=book.author, year=book.year)
    books.append(response)
    return response
