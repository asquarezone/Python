from fastapi import FastAPI
from dotenv import load_dotenv
from app.db.base import Base, engine
from app.api.v1.store import router as store_v1_router

import os

load_dotenv()
Base.metadata.create_all(bind=engine)


# Main application object
# which uvicorn should know about
app = FastAPI(
    title="stores-service",
    description="Store Service with database",
)
app.include_router(store_v1_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv('HOST', 'localhost'),
        port=int(os.getenv('PORT', 8000))
    )
