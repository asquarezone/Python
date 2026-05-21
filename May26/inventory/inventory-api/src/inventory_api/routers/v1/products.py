from fastapi import APIRouter, status
from inventory_api.models import Product

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_products() -> list[Product]:
    return []

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product) -> Product:
    return product