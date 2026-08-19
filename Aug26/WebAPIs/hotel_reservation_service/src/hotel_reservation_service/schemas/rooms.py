"""Pydantic schemas for room-related request and response models."""
from pydantic import BaseModel, Field

class RoomResponse(BaseModel):
    title: str 
    type: str
    price: float
    description: str

