from fastapi import APIRouter
from inventory_api.models import Product

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},)

@router.get("/")
async def read_products() -> list[Product]:
    return []

@router.post("/")
async def create_product(product: Product) -> Product:
    return product