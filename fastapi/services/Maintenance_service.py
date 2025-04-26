from sqlalchemy.orm import Session
import schemas
import Maintenance_Repository

def create_maintenance_service(db: Session, maintenance: schemas.MaintenanceCreate):
    return maintenance_repository.create_maintenance(db, maintenance)

def get_maintenances_service(db: Session):
    return maintenance_repository.get_maintenances(db)

def get_maintenance_by_id_service(db: Session, maintenance_id: int):
    return maintenance_repository.get_maintenance_by_id(db, maintenance_id)