from database import Base
from sqlalchemy import Boolean, Column, Integer, String, Date

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(Date)
    activo = Column(Boolean)