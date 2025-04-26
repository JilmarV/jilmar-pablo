from sqlalchemy.orm import Session
from app import schemas
from app.repositories import car_repository

def create_car_service(db: Session, car: schemas.CarCreate):
    return car_repository.create_car(db, car)

def get_cars_service(db: Session):
    return car_repository.get_cars(db)

def get_car_by_id_service(db: Session, car_id: int):
    return car_repository.get_car_by_id(db, car_id)