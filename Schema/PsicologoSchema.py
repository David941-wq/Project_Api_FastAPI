from pydantic import BaseModel, EmailStr, field_validator
from sqlalchemy.orm import Session
from Models.CitasModels import Cita
from Core.database import SessionLocal
from typing import List, Optional

class PsicologoBase(BaseModel):
    nombre: str
    descripcion: str
    correo: EmailStr
    contraseña: str
    ubicacion: str
    imagen: str
    especialidad: Optional[str] = None
    @field_validator('correo')
    def validacion_correo(cls, value):
        if '@' not in value:
            raise ValueError('El correo electrónico no es válido')
        return value
    
class PsicologoCreate(PsicologoBase):
    pass

class PsicologoResponse(PsicologoBase): 
    id: int

    class Config:
        from_attributes = True