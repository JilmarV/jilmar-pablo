from pydantic import BaseModel
from datetime import datetime

class MaintenanceBase(BaseModel):
    type: str
    notes: str
    car_id: int

class MaintenanceCreate(MaintenanceBase):
    pass

class Maintenance(MaintenanceBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True