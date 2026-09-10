from typing import Annotated
from schemas.tipos import IntPositivo, BoolActivo
from fastapi import APIRouter, Depends, HTTPException, Path, Query

from sqlalchemy.orm import Session

from database import get_db
from models.clientes import Cliente
from schemas.clientes import ClienteSchema, ClienteUpdateSchema

clientes_routers = APIRouter()

NOT_FOUND_RESPONSE = {
    404: {
        "description": "Response not found si no se encuentra el id",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Cliente no encontrado",
                }
            }
        },
    },
}

@clientes_routers.get("/", response_model=list[ClienteSchema])
async def get_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes

@clientes_routers.get(
    "/{id}",
    responses=NOT_FOUND_RESPONSE,
    response_model=ClienteSchema,
)
async def get_clientes_by_id(
    id: IntPositivo, db: Session = Depends(get_db)
):

    cliente_obtenido = db.get(Cliente, id)
    if cliente_obtenido is not None:
        return cliente_obtenido
    raise HTTPException(status_code=404, detail="Artículo no encontrado")



@clientes_routers.post("/", response_model=ClienteSchema) 
async def crear_cliente(
    cliente_nuevo: ClienteSchema, db: Session = Depends(get_db)
): 

    cliente_db = Cliente(
        nombre=cliente_nuevo.nombre,
        apellido=cliente_nuevo.apellido,
        fecha_nacimiento=cliente_nuevo.fecha_nacimiento,
        activo=cliente_nuevo.activo,
    )
    db.add(cliente_db)
    db.commit()
    db.refresh(cliente_db)
    return cliente_db

@clientes_routers.put(
    "/{id}", responses=NOT_FOUND_RESPONSE, response_model=ClienteSchema
)
async def editar_cliente(
    id: IntPositivo,
    cliente_editar: ClienteUpdateSchema,
    db: Session = Depends(get_db),
):

    cliente_obtenido = db.get(Cliente, id)
    if cliente_obtenido is not None:
        cliente_obtenido.nombre = cliente_editar.nombre
        cliente_obtenido.apellido = cliente_editar.apellido
        cliente_obtenido.fecha_nacimiento = cliente_editar.fecha_nacimiento
        cliente_obtenido.activo = cliente_editar.activo
        db.commit()
        db.refresh(cliente_obtenido)
        return cliente_obtenido

    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@clientes_routers.delete(
    "/{id}",
    responses=NOT_FOUND_RESPONSE, 
    response_model=list[ClienteSchema],
)
async def borrar_cliente(
    id: IntPositivo,
    db: Annotated[Session, Depends(get_db)],
    logico: BoolActivo = False,
) -> ClienteSchema:

    cliente_obtenido = db.get(Cliente, id)
    if cliente_obtenido is not None:
        if logico:
            cliente_obtenido.activo = False
        else:
            db.delete(cliente_obtenido)
            db.commit()
        return db.query(Cliente).all()
    raise HTTPException(status_code=404, detail="Cliente no encontrado")