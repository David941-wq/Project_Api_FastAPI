from pydantic import BaseModel, EmailStr


class PsicologoBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    correo: EmailStr
    localidad_id: int
    especialidad: str
    imagen: str | None = None


class PsicologoCreate(PsicologoBase):
    contraseña: str


class PsicologoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None
    correo: EmailStr
    localidad_id: int
    especialidad: str
    imagen: str | None = None
    activo: bool

    class Config:
        from_attributes = True
