from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Core.database import SessionLocal, get_db
from Core.deps import obtener_usuario_actual, obtener_psicologo_actual 
from typing import List

from Schema.PsicologoSchema import PsicologoCreate, PsicologoResponse
from Schema.UsuarioSchema import UsuarioCreate, UsuarioResponse
from Schema.CitasSchema import CitasCreate, CitasResponse
from Schema.NumerEmergencia import NumeroEmergenciaResponse
from Schema.loginSchema import LoginResponse, LoginCreate
from Schema.CitasSchema import CitasResponse
from Schema.LocalidadSchema import LocalidadResponse

from service.PsicologoService import PsicologoService
from service.UsuarioService import UsuarioService
from service.CItasService import CitasService
from service.NumeroEService import NumeroEService
from service.LocalidadService import LocalidadService

router = APIRouter()
Psicologo = PsicologoService()
Usuarios= UsuarioService()
Citas = CitasService()
NumerosE = NumeroEService()
localidad_service = LocalidadService()



# 🔍 Obtener todos los psicólogos

@router.get("/psicologos", response_model=List[PsicologoResponse])
def get_psicologos(db: Session = Depends(get_db)):
    return Psicologo.listar_psicologos(db)

@router.post("/psicologos", response_model=PsicologoResponse)
def crear_psicologo(id: int, db: Session = Depends(get_db)):
    return Psicologo.obtener_psicologo_por_id(db, id)

@router.get("/psicologos/{id}", response_model=PsicologoResponse)
def obtener_psicologo(id: int, db: Session = Depends(get_db)):
    return Psicologo.obtener_psicologo_por_id(db, id)

@router.get("/psicologos/mias/citas", response_model=List[CitasResponse])
def obtener_citas_mias(psicologo_actual=Depends(obtener_psicologo_actual), db: Session = Depends(get_db)):
    return Citas.obtener_citas_por_psicologo(db, psicologo_actual)

#-------------------------------------------------------------------
# Usuarios
#-------------------------------------------------------------------

@router.get("/usuarios", response_model=List[UsuarioResponse])
def get_usuarios(db: Session = Depends(get_db)):
    return Usuarios.listar_usuarios(db)

@router.post("/usuarios", response_model=UsuarioResponse)
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return Usuarios.crear_usuario(db, data)

@router.get("/usuarios/{id}", response_model=UsuarioResponse)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    return Usuarios.obtener_usuario_por_id(db, id)

@router.get("/usuarios/mias/citas", response_model=List[CitasResponse])
def obtener_citas_mias(usuario_actual=Depends(obtener_usuario_actual),db: Session = Depends(get_db)):
    return Usuarios.obtener_citas_por_usuario(db, usuario_actual.id)
#-------------------------------------------------------------------
# Citas
#-------------------------------------------------------------------

@router.post("/citas", response_model=CitasResponse)
def crear_cita(data: CitasCreate, usuario_actual=Depends(obtener_usuario_actual),db: Session = Depends(get_db)):
    return Citas.crear_cita(db, data, usuario_actual)

@router.get("/citas/{id}", response_model=CitasResponse)
def obtener_cita(id: int, db: Session = Depends(get_db)):
    return Citas.obtener_cita_por_id(db, id)

@router.get("/citas/mias/todas", response_model=List[CitasResponse])
def obtener_citas_mias(usuario_actual=Depends(obtener_usuario_actual),db: Session = Depends(get_db)):
    return Citas.obtener_citas_por_usuario(db, usuario_actual)

@router.put("/citas/{id}/fecha", response_model=CitasResponse)
def cambiar_fecha_cita(id: int, nueva_fecha: str, usuario_actual=Depends(obtener_usuario_actual),db: Session = Depends(get_db)):
    return Citas.cambiar_fecha_cita(db, id, nueva_fecha, usuario_actual)

@router.put("/citas/{id}/estado", response_model=CitasResponse)
def cambiar_estado_cita(id: int, nuevo_estado: str, psicologo_actual=Depends(obtener_psicologo_actual),db: Session = Depends(get_db)):
    return Citas.cambiar_estado_cita(db, id, nuevo_estado, psicologo_actual)

#-------------------------------------------------------------------
# Numeros de emergencia
#-------------------------------------------------------------------

@router.get("/numeros-emergencia/localidad/{localidad_id}", response_model=List[NumeroEmergenciaResponse])
def obtener_numeros_por_localidad(localidad_id: int, db: Session = Depends(get_db)):
    return NumerosE.obtener_por_localidad(db, localidad_id)

@router.get("/numeros-emergencia/mios", response_model=List[NumeroEmergenciaResponse])
def mis_numeros_emergencia(
    usuario_actual=Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    return NumerosE.obtener_mis_numeros_emergencia(db, usuario_actual)

#-------------------------------------------------------------------
# Numeros de emergencia
#-------------------------------------------------------------------

@router.get("/localidades", response_model=List[LocalidadResponse])
def obtener_localidades(db: Session = Depends(get_db)):
    return localidad_service.listar_localidades(db)