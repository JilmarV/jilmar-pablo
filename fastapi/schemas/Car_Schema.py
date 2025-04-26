from pydantic import BaseModel
from typing import List
from maintenance import Maintenance

class Car_Schema(BaseModel):
    brand: str
    model: str
    year: int
    fuel_type: str  # 'regular' or 'diesel'

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    maintenances: List[Maintenance] = []

    class Config:
        orm_mode = True