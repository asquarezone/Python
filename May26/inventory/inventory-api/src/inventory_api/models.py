from pydantic import BaseModel, EmailStr, AnyUrl, Field


class ProductRequest(BaseModel):
    name: str = Field(min_length=3, max_length=5)
    description: str
    price: float = Field(default=0.0, gt=0, lt=10000)


class ProductResponse(ProductRequest):
    id: int
    
class User(BaseModel):
    id: str
    name: str
    email: EmailStr


class Supplier(BaseModel):
    id: str
    name: str
    url: AnyUrl