"""Entry point for the Hotel Reservation Service FastAPI application."""
from fastapi import FastAPI
from hotel_reservation_service.api.v1.room import room_v1_router

app = FastAPI(title="hotel-reservation-service")

app.include_router(
    room_v1_router,
    prefix="/api/v1"
)