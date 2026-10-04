from sqlmodel import Field, SQLModel, Relationship

from datetime import date

from .servicio import Servicio


class ClienteBase(SQLModel):

    nombre: str = Field(max_length=90)

    apellido: str = Field(max_length=90)

    fecha_nacimiento: date

    activo: bool

    servicio_id: int | None = Field(
        default=None,
        foreign_key="servicio.id"
    )


class Cliente(ClienteBase, table=True):

    id: int | None = Field(default=None, primary_key=True)

    servicio: Servicio | None = Relationship(
        back_populates="clientes"
    )


class ClientePublic(ClienteBase):

    id: int

    