from fastapi import APIRouter, HTTPException, status
from app.schemas.store import StoreRequest, StoreResponse
from app.repository.store import create_store as db_create_store
from app.repository.store import get_all_stores as db_get_all_stores

router = APIRouter(
    prefix="/api/v1/stores",
    tags=["Store"]
)


@router.post("/", response_model=StoreResponse, status_code=status.HTTP_201_CREATED)
def create_store(request: StoreRequest) -> StoreResponse:
    return db_create_store(request)

@router.get("/", response_model=list[StoreResponse])
def get_all_stores() -> list[StoreResponse]:
    return db_get_all_stores()
