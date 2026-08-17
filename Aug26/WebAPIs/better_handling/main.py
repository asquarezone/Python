from fastapi import (
    FastAPI, Path, Query, Form, File, UploadFile
)
from typing import Annotated, Literal
from enum import Enum
from schemas import UserRequest, UserResponse
import uuid



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


# Query Parameters
@app.get("/items")
def get_item(id: Annotated[int, Query(ge=1, le=1000)], price: Literal["min", "moderate", "high"]):
    return {"id": id, "price": price}


@app.post("/users")
def create_user(user: UserRequest) -> UserResponse:
    return UserResponse(**user.model_dump(), id=uuid.uuid4())


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}