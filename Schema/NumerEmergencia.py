from pydantic import BaseModel


class NumeroEmergenciaResponse(BaseModel):
    id: int
    nombre: str
    numero: str
    localidad_id: int

    class Config:
        from_attributes = True
