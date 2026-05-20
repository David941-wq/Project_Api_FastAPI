from pydantic import BaseModel, EmailStr, field_validator
from sqlalchemy.orm import Session
from Core.database import SessionLocal
from typing import Optional

class NumeroEmergenciaResponse(BaseModel):
    id: int
    numero: int
    localidad_id: int
    localidad_nombre: Optional[str] = None

    class Config:
        orm_mode = True