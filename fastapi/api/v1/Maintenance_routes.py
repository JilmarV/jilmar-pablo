from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import schemas 
import maintenance_service

router = APIRouter(
    prefix="/maintenances",
    tags=["maintenances"]
)

@router.post("/", response_model=schemas.Maintenance)
def create_maintenance(maintenance: schemas.MaintenanceCreate, db: Session = Depends(get_db)):
    return maintenance_service.create_maintenance_service(db, maintenance)

@router.get("/", response_model=list[schemas.Maintenance])
def list_maintenances(db: Session = Depends(get_db)):
    return maintenance_service.get_maintenances_service(db)

@router.get("/{maintenance_id}", response_model=schemas.Maintenance)
def get_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    maintenance = maintenance_service.get_maintenance_by_id_service(db, maintenance_id)
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    return maintenance