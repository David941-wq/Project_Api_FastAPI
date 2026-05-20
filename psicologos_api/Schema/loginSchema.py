from pydantic import BaseModel


class LoginCreate(BaseModel):
    nombre: str
    contraseña: str

class LoginResponse(BaseModel):
    usuario_id: int
    nombre: str

    class Config:
        from_attributes = True