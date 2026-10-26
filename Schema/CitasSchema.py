from pydantic import BaseModel
from datetime import date as date_type, time as time_type
from Models.CitasModels import EstadoCita


class CitasBase(BaseModel):
    date: date_type
    hour: time_type
    description: str | None = None


class CitasCreate(CitasBase):
    psicologo_id: int
    # usuario_id NO va aquí: se obtiene del token (usuario_actual)


class CitasResponse(CitasBase):
    id: int
    status: EstadoCita
    usuario_id: int
    psicologo_id: int

    class Config:
        from_attributes = True


class CitaFechaUpdate(BaseModel):
    date: date_type
    hour: time_type | None = None
