from pydantic import BaseModel, Field
from .tipos import BoolActivo, StrCortito, Fecha, IntPositivo

class ClienteSchema(BaseModel):
    id: IntPositivo
    nombre: StrCortito
    apellido: StrCortito
    fecha_nacimiento: Fecha
    activo: BoolActivo

class ClienteUpdateSchema(BaseModel):
    nombre: StrCortito
    apellido: StrCortito
    fecha_nacimiento: Fecha
    activo: BoolActivo