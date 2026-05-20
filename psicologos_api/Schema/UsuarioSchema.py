from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from sqlalchemy.orm import Session
from Models.Models import Usuario
from Core.database import SessionLocal

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    contraseña: str
    ubicacion: str
    localidad_id: int
    telefono: Optional[str] = None

    @field_validator('contraseña')
    def validacion_contraseña(cls, values):
        if len(values) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        return values
    
    
class UsuarioCreate(UsuarioBase):
        pass

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    ubicacion: str
    telefono: Optional[str] = None
    localidad_id: int

    class Config:
        from_attributes = True