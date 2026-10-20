from pydantic import BaseModel
from datetime import date, time
from Models.CitasModels import EstadoCita

# terminar los schemas para que las peticiones den resultados optimos

class CitasBase(BaseModel):
    date: date
    hour: time
    description: str | None = None

class CitasCreate(CitasBase):
    psicologo_id: int
    pass

class CitasResponse(BaseModel):
    id: int
    status: EstadoCita
    usuario_id: int
    psicologo_id: int

    class Config:
        from_attributes = True

class CitasUpdate(BaseModel):
    date: date 
    hour: time | None = None