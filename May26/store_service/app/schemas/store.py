from typing import List, Optional
from pydantic import BaseModel, Field

class StoreRequest(BaseModel):
    name: str = Field(..., max_length=50, min_length=2)
    city: str = Field(..., max_length=50, min_length=2)
    area: str = Field(..., max_length=200, min_length=5)
    address: str = Field(..., max_length=200, min_length=5)


class StoreResponse(StoreRequest):
    id: int

