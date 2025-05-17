"""This module is the main or startup for Application
"""

from fastapi import FastAPI
from database import Base, engine
from movies import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movie Service",
    summary="Movie Service",
    description="Movie Service",
    version="1.0.0"
)

app.include_router(router=router, prefix="/v1")