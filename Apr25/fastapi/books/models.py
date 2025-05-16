from pydantic import BaseModel, Field


class BookBody(BaseModel):
    """Book Request Model
    """
    title: str = Field(...,min_length=1, max_length=100)
    author: str = Field(...,min_length=1, max_length=100)
    year: int = Field(..., gt=0, lt=2100)

# class BookResponse(Book):
#     """Book Response model
#     """
#     book_id: int = Field(..., gt=0)
