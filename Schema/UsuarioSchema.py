from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: str | None = None
    localidad_id: int


class UsuarioCreate(UsuarioBase):
    password: str = Field(min_length=6)


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    telefono: str | None = None
    activo: bool
    localidad_id: int

    class Config:
        from_attributes = True
