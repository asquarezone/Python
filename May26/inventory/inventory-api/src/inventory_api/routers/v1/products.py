from fastapi import APIRouter, status
from inventory_api.models import ProductRequest, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_products() -> list[ProductResponse]:
    return []

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductRequest) -> ProductResponse:
    return ProductResponse(**product.model_dump(), id = 1)