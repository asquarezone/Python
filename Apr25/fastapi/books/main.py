from fastapi import FastAPI

app = FastAPI(
    title="BookStore",
    summary="Books store for learning",
    description="FastAPI for books store",
    version="0.0.1"
)

@app.get("/books")
async def get_all_books():
    return []

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    return {
        "book_id": book_id,
        "title": "Your brain at work",
        "author": "David Rock"
    }
