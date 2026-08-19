"""Room-specific API routes for v1 of the Hotel Reservation Service."""

from fastapi.routing import APIRouter
from hotel_reservation_service.schemas.rooms import RoomResponse

room_v1_router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"],
)

@room_v1_router.get("/", response_model=list[RoomResponse])
def get_rooms():
    return []