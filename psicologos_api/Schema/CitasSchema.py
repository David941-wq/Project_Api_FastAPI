from pydantic import BaseModel
from datetime import date, time


class CitasBase(BaseModel):
    psicologo_id: int
    usuario_id: int
    fecha: str
    hora: str

class CitasCreate(CitasBase):
    pass

class CitasResponse(BaseModel):
    id: int
    psicologo_id: int
    usuario_id: int
    fecha: date
    hora: time

    class Config:
        from_attributes = True