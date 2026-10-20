from pydantic import BaseModel

class LoginBase(BaseModel):
    nombre: str
    contraseña: str

class LoginCreate(LoginBase):
    pass

class LoginResponse(BaseModel):
    usuario_id: int
    nombre: str

    class Config:
        from_attributes = True