"""This module has schemas for request and response in API 
"""

from pydantic import BaseModel


class MovieBase(BaseModel):
    """Base model
    """
    title: str
    description: str | None = None
    language: str
    duration: float
    rating: float


class MovieRequest(MovieBase):
    """This represent the Request of movie
    in the api 
    """


class MovieResponse(MovieBase):
    """This represents the response from movie
    apis
    """
    id: int

    class config:
        orm_mode = True
