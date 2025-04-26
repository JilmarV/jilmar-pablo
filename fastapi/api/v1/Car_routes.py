from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.services import car_service

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)

@router.post("/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return car_service.create_car_service(db, car)

@router.get("/", response_model=list[schemas.Car])
def list_cars(db: Session = Depends(get_db)):
    return car_service.get_cars_service(db)

@router.get("/{car_id}", response_model=schemas.Car)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = car_service.get_car_by_id_service(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car