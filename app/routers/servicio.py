from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from database import get_db
from models.anidados import ServicioNested

from models.servicio import Servicio, ServicioPublic, ServicioBase

servicio_routers = APIRouter()

@servicio_routers.get("/", response_model=list[ServicioNested])
async def get_(db: Session = Depends(get_db)):
    clientes = db.exec(select(Servicio)).all()
    return clientes


@servicio_routers.post(
    "/servicio", response_model=ServicioPublic
) 
async def crear_servicio(servicio: ServicioBase, db: Session = Depends(get_db)):
    nuevo_servicio = Servicio.model_validate(servicio)

    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio

