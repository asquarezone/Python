from fastapi import FastAPI, Header
from pydantic import BaseModel
from inventory_api.models import (
    Product, 
    User, 
    Supplier
) 


app = FastAPI(title="Inventory API")

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/products")
async def create_product(product: Product):
    return product


@app.post("/users")
async def create_user(user: User):
    return user

@app.post("/suppliers")
async def create_supplier(supplier: Supplier):
    return supplier


@app.get("/products/")
async def get_products(category:str, limit:int = 10):
    return {
        "category": category,
        "limit": limit
    }


@app.get("/profile")
async def profile(authorization: str = Header(), version: str = Header(default='v1')):
    return { 
        "recieved_token": authorization,
        "version": version
    }
