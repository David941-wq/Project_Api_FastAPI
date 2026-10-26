from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Core.database import get_db
from Core.deps import obtener_usuario_actual, obtener_psicologo_actual
from typing import List

from Schema.PsicologoSchema import PsicologoCreate, PsicologoResponse
from Schema.UsuarioSchema import UsuarioCreate, UsuarioResponse
from Schema.CitasSchema import CitasCreate, CitasResponse, CitaFechaUpdate
from Schema.NumerEmergencia import NumeroEmergenciaResponse
from Schema.loginSchema import LoginResponse, LoginCreate
from Schema.LocalidadSchema import LocalidadResponse
from Schema.ComentarioSchema import (
    ComentarioCreate, ComentarioResponse,
    RespuestaComentarioCreate, RespuestaComentarioResponse,
    ContenidoUpdate
)

from service.PsicologoService import PsicologoService
from service.UsuarioService import UsuarioService
from service.CitasService import CitasService
from service.NumeroEService import NumeroEService
from service.LocalidadService import LocalidadService
from service.ComentarioService import ComentarioService
from service.RespuestaComentarioService import RespuestaComentarioService

router = APIRouter()

psicologo_service = PsicologoService()
usuario_service = UsuarioService()
citas_service = CitasService()
numero_e_service = NumeroEService()
localidad_service = LocalidadService()
comentario_service = ComentarioService()
respuesta_service = RespuestaComentarioService()

# -------------------------------------------------------------------
# Psicólogos
# -------------------------------------------------------------------

@router.get("/psicologos", response_model=List[PsicologoResponse], tags=["Psicólogos"])
def get_psicologos(db: Session = Depends(get_db)):
    return psicologo_service.listar_psicologos(db)

@router.post("/psicologos", response_model=PsicologoResponse, tags=["Psicólogos"])
def crear_psicologo(data: PsicologoCreate, db: Session = Depends(get_db)):
    return psicologo_service.crear_psicologo(db, data)

@router.get("/psicologos/{id}", response_model=PsicologoResponse, tags=["Psicólogos"])
def obtener_psicologo(id: int, db: Session = Depends(get_db)):
    return psicologo_service.obtener_psicologo_por_id(db, id)

@router.get("/psicologos/mias/citas", response_model=List[CitasResponse], tags=["Psicólogos"])
def obtener_citas_mias_psicologo(
    psicologo_actual=Depends(obtener_psicologo_actual),
    db: Session = Depends(get_db)
):
    return citas_service.listar_por_psicologo(db, psicologo_actual)

@router.post("/psicologos/login", response_model=LoginResponse, tags=["Psicólogos"])
def login_psicologo(datos: LoginCreate, db: Session = Depends(get_db)):
    return psicologo_service.login(db, datos)

# -------------------------------------------------------------------
# Usuarios
# -------------------------------------------------------------------

@router.get("/usuarios", response_model=List[UsuarioResponse], tags=["Usuarios"])
def get_usuarios(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)

@router.post("/usuarios", response_model=UsuarioResponse, tags=["Usuarios"])
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.crear_usuario(db, data)

@router.get("/usuarios/{id}", response_model=UsuarioResponse, tags=["Usuarios"])
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    return usuario_service.obtener_usuario_por_id(db, id)

@router.post("/login", response_model=LoginResponse, tags=["Usuarios"])
def login(datos: LoginCreate, db: Session = Depends(get_db)):
    return usuario_service.login(db, datos)

# -------------------------------------------------------------------
# Citas
# -------------------------------------------------------------------

@router.post("/citas", response_model=CitasResponse, tags=["Citas"])
def crear_cita(
    data: CitasCreate,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return citas_service.crear_cita(db, data, usuario_actual)

@router.get("/citas/{id}", response_model=CitasResponse, tags=["Citas"])
def obtener_cita(id: int, db: Session = Depends(get_db)):
    return citas_service.obtener_cita_por_id(db, id)

@router.get("/citas/mias/todas", response_model=List[CitasResponse], tags=["Citas"])
def mis_citas(
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return citas_service.listar_mis_citas(db, usuario_actual)

@router.put("/citas/{id}/fecha", response_model=CitasResponse, tags=["Citas"])
def cambiar_fecha_cita(
    id: int,
    data: CitaFechaUpdate,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return citas_service.cambiar_fecha_hora(db, id, data.date, data.hour, usuario_actual)

@router.put("/citas/{id}/cancelar", response_model=CitasResponse, tags=["Citas"])
def cancelar_cita(
    id: int,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return citas_service.cancelar_cita(db, id, usuario_actual)

# -------------------------------------------------------------------
# Números de emergencia
# -------------------------------------------------------------------

@router.get(
    "/numeros-emergencia/localidad/{localidad_id}",
    response_model=List[NumeroEmergenciaResponse],
    tags=["Números de emergencia"]
)
def obtener_numeros_por_localidad(localidad_id: int, db: Session = Depends(get_db)):
    return numero_e_service.obtener_por_localidad(db, localidad_id)

@router.get(
    "/numeros-emergencia/mios",
    response_model=List[NumeroEmergenciaResponse],
    tags=["Números de emergencia"]
)
def mis_numeros_emergencia(
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return numero_e_service.obtener_mis_numeros_emergencia(db, usuario_actual)

# -------------------------------------------------------------------
# Localidades
# -------------------------------------------------------------------

@router.get("/localidades", response_model=List[LocalidadResponse], tags=["Localidades"])
def obtener_localidades(db: Session = Depends(get_db)):
    return localidad_service.listar_localidades(db)

# -------------------------------------------------------------------
# Comentarios
# -------------------------------------------------------------------

@router.post("/comentarios", response_model=ComentarioResponse, tags=["Comentarios"])
def crear_comentario(
    data: ComentarioCreate,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return comentario_service.crear_comentario(db, data, usuario_actual)

@router.get("/comentarios", response_model=List[ComentarioResponse], tags=["Comentarios"])
def listar_comentarios(db: Session = Depends(get_db)):
    return comentario_service.listar_comentarios(db)

@router.get("/comentarios/{id}", response_model=ComentarioResponse, tags=["Comentarios"])
def obtener_comentario(id: int, db: Session = Depends(get_db)):
    return comentario_service.obtener_comentario_por_id(db, id)

@router.put("/comentarios/{id}", response_model=ComentarioResponse, tags=["Comentarios"])
def actualizar_comentario(
    id: int,
    data: ContenidoUpdate,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return comentario_service.actualizar_comentario(db, id, usuario_actual, data.contenido)

@router.delete("/comentarios/{id}", response_model=ComentarioResponse, tags=["Comentarios"])
def eliminar_comentario(
    id: int,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return comentario_service.desactivar_comentario(db, id, usuario_actual)

# -------------------------------------------------------------------
# Respuestas a comentarios
# -------------------------------------------------------------------

@router.post("/respuestas", response_model=RespuestaComentarioResponse, tags=["Respuestas"])
def crear_respuesta(
    data: RespuestaComentarioCreate,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return respuesta_service.crear_respuesta(db, data, usuario_actual)

@router.get(
    "/respuestas/comentario/{comentario_id}",
    response_model=List[RespuestaComentarioResponse],
    tags=["Respuestas"]
)
def listar_respuestas(comentario_id: int, db: Session = Depends(get_db)):
    return respuesta_service.listar_respuestas_por_comentario(db, comentario_id)

@router.put("/respuestas/{id}", response_model=RespuestaComentarioResponse, tags=["Respuestas"])
def actualizar_respuesta(
    id: int,
    data: ContenidoUpdate,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return respuesta_service.actualizar_respuesta(db, id, usuario_actual, data.contenido)

@router.delete("/respuestas/{id}", response_model=RespuestaComentarioResponse, tags=["Respuestas"])
def eliminar_respuesta(
    id: int,
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return respuesta_service.desactivar_respuesta(db, id, usuario_actual)
