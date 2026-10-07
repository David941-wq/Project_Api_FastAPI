from pydantic import BaseModel, EmailStr


class LoginCreate(BaseModel):
    correo: EmailStr
    contraseña: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    usuario_id: int | None = None
    psicologo_id: int | None = None
    nombre: str
