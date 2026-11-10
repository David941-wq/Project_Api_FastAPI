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

class ComentarioConLikesResponse(ComentarioResponse):
    likes: int = 0
    liked: bool = False


class LikeResponse(BaseModel):
    comentario_id: int
    likes: int
    liked: bool


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

class RespuestaConLikesResponse(RespuestaComentarioResponse):
    likes: int = 0
    liked: bool = False


class LikeRespuestaResponse(BaseModel):
    respuesta_id: int
    likes: int
    liked: bool

class ContenidoUpdate(BaseModel):
    contenido: str
