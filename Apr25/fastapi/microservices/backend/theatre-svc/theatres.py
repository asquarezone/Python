from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Theatre, Screen
from schemas import TheatreRequest, ScreenRequest, TheatreResponse, ScreenResponse

router = APIRouter()


def get_db():
    """Gets the database connection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/theatres")
def list_theatres(db: Session = Depends(get_db)) -> list[TheatreResponse]:
    """This method responds to Get All theatres
    """
    return db.query(Theatre).all()


@router.get("/theatres/{theatre_id}")
def get_theatre(theatre_id: int, db: Session = Depends(get_db)) -> TheatreResponse:
    """This method gets a specific theatres
    """
    theatre = (
        db.query(Theatre).filter(Theatre.id == theatre_id).first()
    )
    if theatre is None:
        raise HTTPException(
            status_code=404,
            detail="Movie Not Found"
        )
    return theatre


@router.post("/theatres")
def create_theatre(theatre: TheatreRequest, db: Session = Depends(get_db)) -> TheatreResponse:
    """This method creates a theatres
    """
    new_theatre = Theatre(**theatre.model_dump())
    db.add(new_theatre)
    db.commit()
    db.refresh(new_theatre)
    return new_theatre


@router.get("/theatres/{theatre_id}/screens")
def get_screens(theatre_id: int, db: Session = Depends(get_db)) -> list[ScreenResponse]:
    """This method will get the screens of a theatre
    """
    return db.query(Screen).filter(Screen.theatre_id == theatre_id).all()


@router.post("/screens")
def create_screen(screen: ScreenRequest, db: Session = Depends(get_db)) -> ScreenResponse:
    """This method will get the screens of a theatre
    """
    new_screen = Screen(**screen.model_dump())
    db.add(new_screen)
    db.commit()
    db.refresh(new_screen)
    return new_screen
