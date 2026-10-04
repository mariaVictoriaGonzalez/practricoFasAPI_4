from sqlmodel import Field, Relationship, SQLModel


class ServicioBase(SQLModel):
    nombre: str = Field(max_length=90)
    detalle: str


class Servicio(ServicioBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    clientes: "Cliente" = Relationship(back_populates="servicio")


class ServicioPublic(ServicioBase):
    id: int

