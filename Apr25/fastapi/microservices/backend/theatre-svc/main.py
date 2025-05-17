"""This module is the main or startup for Application
"""

from fastapi import FastAPI
from database import Base, engine
from theatres import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Theatre Service",
    summary="Theatre Service",
    description="Theatre Service",
    version="1.0.0"
)

app.include_router(router=router, prefix="/v1")