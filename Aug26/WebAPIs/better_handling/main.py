from fastapi import (
    FastAPI, Path, Query, Form, File, UploadFile, Header, Cookie
)
from typing import Annotated, Literal
from enum import Enum
from schemas import UserRequest, UserResponse
import uuid
from v1routes import product_router, order_router
from v2routes import product_router as product_router_v2, order_router as order_router_v2



app = FastAPI(
    title="Learning",
    description="A simple API to handle rest api requests",
    version="1.0.0")

#app.include_router(product_router, prefix="/api/v1")
#app.include_router(order_router, prefix="/api/v1")

app.include_router(product_router_v2, prefix="/api/v2")
app.include_router(order_router_v2, prefix="/api/v2")

# PATH Parameters

# @app.get("/products/{product_id}")
# def get_product(product_id: int):
#     return {"product_id": product_id}


# @app.get("/products/{product_id}")
# def get_product(product_id: Annotated[int, Path(ge=1, le=100)]):
#     return {"product_id": product_id}


# @app.get("/complaints/{severity}")  
# def get_complaints(severity: Literal["low", "medium", "high"]):
#     return {"severity": severity}

# class Offer(str, Enum):
#     today = "today"
#     week = "week"
#     month = "month"

# @app.get("/offers/{offer}")
# def get_offers(offer: Offer):
#     return {"offer": offer}


# # Query Parameters
# @app.get("/items")
# def get_item(id: Annotated[int, Query(ge=1, le=1000)], price: Literal["min", "moderate", "high"]):
#     return {"id": id, "price": price}


# @app.post("/users")
# def create_user(user: UserRequest) -> UserResponse:
#     return UserResponse(**user.model_dump(), id=uuid.uuid4())


# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

# @app.get("/whoami/")
# async def whoami(useragent:
#     Annotated[str, Header(alias="User-Agent")]):
#     return {"user-agent": useragent}


# @app.get("/ea/")
# async def register(eaversion: Annotated[str, Header(alias="ea-version")]):
#     return {"ea-version": eaversion}