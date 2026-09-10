from datetime import date
from typing import Annotated
from pydantic import Field


IntPositivo = Annotated[int, Field(gt=0)]
StrCortito = Annotated[str, Field(max_length=30)]
Fecha = Annotated[date, Field()]
BoolActivo = Annotated[bool, Field(description="Sigue disponible?")]
