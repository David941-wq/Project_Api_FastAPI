from pydantic import BaseModel
from datetime import datetime


class ComentarioCreate(BaseModel):
    contenido: str
    # usuario_id NO va aquí: se obtiene del token (usuario_actual)


class ComentarioResponse(BaseModel):
    id: int
    contenido: str
    activo: bool
    usuario_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class RespuestaComentarioCreate(BaseModel):
    contenido: str
    comentario_id: int
    # usuario_id NO va aquí: se obtiene del token (usuario_actual)


class RespuestaComentarioResponse(BaseModel):
    id: int
    contenido: str
    activo: bool
    comentario_id: int
    usuario_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ContenidoUpdate(BaseModel):
    contenido: str
