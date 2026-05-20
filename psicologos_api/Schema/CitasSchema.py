from pydantic import BaseModel
from pydantic import EmailStr
from datetime import date, time


class CitasBase(BaseModel):
    nombre_paciente: str
    correo: EmailStr
    psicologo_id: int
    usuario_id: int
    fecha: date
    hora: time
    motivo: str | None

class CitasCreate(CitasBase):
    pass

class CitasResponse(BaseModel):
    id: int
    nombre_paciente: str
    correo: EmailStr
    psicologo_id: int
    usuario_id: int
    fecha: date
    hora: time
    motivo: str | None

    class Config:
        from_attributes = True