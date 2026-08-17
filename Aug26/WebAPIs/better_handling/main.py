from fastapi import (
    FastAPI, Path
)
from typing import Annotated, Literal
from enum import Enum




app = FastAPI(
    title="Learning",
    description="A simple API to handle rest api requests",
    version="1.0.0")

# PATH Parameters

# @app.get("/products/{product_id}")
# def get_product(product_id: int):
#     return {"product_id": product_id}


@app.get("/products/{product_id}")
def get_product(product_id: Annotated[int, Path(ge=1, le=100)]):
    return {"product_id": product_id}


@app.get("/complaints/{severity}")  
def get_complaints(severity: Literal["low", "medium", "high"]):
    return {"severity": severity}

class Offer(str, Enum):
    today = "today"
    week = "week"
    month = "month"

@app.get("/offers/{offer}")
def get_offers(offer: Offer):
    return {"offer": offer}