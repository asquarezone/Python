from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Movie
from schemas import MovieRequest

router = APIRouter()

def get_db():
    """Gets the database connection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/movies")
def list_movies(db: Session = Depends(get_db)):
    """This method responds to Get All movies
    """
    return db.query(Movie).all()

@router.get("/movies/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """This method gets a specific movie
    """
    movie = (
        db.query(Movie).filter(Movie.id == movie_id).first()
    )
    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    return movie

@router.post("/movies")
def create_movie(movie: MovieRequest, db: Session = Depends(get_db)):
    """This method creates a movie
    """
    new_movie = Movie(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
