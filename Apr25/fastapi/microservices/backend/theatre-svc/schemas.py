"""This module has schemas for request and response in API 
"""

from pydantic import BaseModel


class TheatreBase(BaseModel):
    """Base model
    """
    name: str
    location: str


class TheatreRequest(TheatreBase):
    """This represent the Request of movie
    in the api 
    """


class MovieResponse(TheatreBase):
    """This represents the response from movie
    apis
    """
    id: int

    class config:
        orm_mode = True
