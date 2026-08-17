from fastapi import APIRouter

product_router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@product_router.get("/")
def get_products():
    return {"message": "Hello Products"}

order_router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@order_router.get("/")
def get_orders():
    return {"message": "Hello Orders"}