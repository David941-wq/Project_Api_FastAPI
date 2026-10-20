from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from sqlalchemy.orm import Session
from Models.UserModels import User
from Core.database import SessionLocal

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    password: str
    ubicacion: str
    localidad_id: int
    telefono: Optional[str] = None

    @field_validator('password')
    def validacion_contraseña(cls, values):
        if len(values) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        return values
    
    
class UsuarioCreate(UsuarioBase):
        pass

class UsuarioResponse(BaseModel):
    nombre: str
    correo: EmailStr
    ubicacion: str
    telefono: Optional[str] = None

    class Config:
        from_attributes = True