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


class TheatreResponse(TheatreBase):
    """This represents the response from movie
    apis
    """
    id: int

    class config:
        orm_mode = True


class ScreenBase(BaseModel):
    """Base Schema for Screens
    """
    name: str
    theatre_id: int

class ScreenRequest(ScreenBase):
    """This represents the request to screen apis
    """

class ScreenResponse(ScreenBase):
    """This represents the response to screen api
    """
    id: int
    
    class Config:
        orm_mode = True
