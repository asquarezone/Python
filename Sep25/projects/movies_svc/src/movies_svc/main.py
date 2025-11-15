import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from contextlib import asynccontextmanager
from typing import Annotated, AsyncGenerator

from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, status

load_dotenv()

### Database Configuration

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql+asyncpg://postgres:postgres@localhost:5432/movies_db'
)

### Database Models
class Base(DeclarativeBase): pass

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    director: Mapped[str] = mapped_column(String(120))




## Request models

class MovieRequest(BaseModel):
    title: str
    director: str

class MovieResponse(MovieRequest):
    id: int
    class Config:
        orm_mode = True  # works with FastAPI to read from ORM objects


### Database engine

# Async SQLAlchemy engine and session factory
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency that provides an async DB session."""
    async with AsyncSessionLocal() as session:
        yield session


### when fastapi starts we need schema to be created if not present
# ============================================================
# FastAPI app + lifespan (startup/shutdown)
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan handler runs on startup and shutdown.

    Here we auto-create tables on startup (for demo).
    In real projects, prefer Alembic migrations.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # (No special shutdown logic needed here)

app = FastAPI(
    title="Movies API (FastAPI + Async SQLAlchemy + Postgres)",
    lifespan=lifespan,
)



@app.get("/movies", response_model=list[MovieResponse])
async def list_movies(session: Annotated[AsyncSession, Depends(get_session)]):
    result = await session.execute(select(Movie))
    movies = result.scalars().all()
    return movies

# @app.get("/movies/{movie_id}", response_model=MovieResponse)
# async def get_movie_by_id(movie_id:int):
#     for movie in movies:
#         if movie.id == movie_id:
#             return movie
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Movie not found")

@app.post("/movies", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
async def create_movie(
        movie: MovieRequest,
        session: Annotated[AsyncSession, Depends(get_session)]
    ):
    db_movie = Movie(**movie.model_dump())
    session.add(db_movie)
    await session.commit()
    await session.refresh(db_movie)
    return db_movie