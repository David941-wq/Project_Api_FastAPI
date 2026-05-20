from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Core.database import engine, SessionLocal, Base
from typing import List

from Schema.PsicologoSchema import PsicologoCreate, PsicologoResponse
from Schema.UsuarioSchema import UsuarioCreate, UsuarioResponse
from Schema.CitasSchema import CitasCreate, CitasResponse
from Schema.NumerEmergencia import NumeroEmergenciaResponse

from service.service import PsicologoService, UsuarioService, CitasService, NumeroEmergenciaService

Base.metadata.create_all(bind=engine)

router = APIRouter()
Psicologos = PsicologoService()
Usuarios= UsuarioService()
Citas = CitasService()
NumerosE = NumeroEmergenciaService()

# Dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔍 Obtener todos los psicólogos
@router.get("/psicologos", response_model=List[PsicologoResponse])
def get_psicologos(db: Session = Depends(get_db)):
    return Psicologos.Listar_psicologos(db)

# ➕ Crear psicólogo
@router.post("/psicologos", response_model=PsicologoResponse)
def crear_psicologo(data: PsicologoCreate, db: Session = Depends(get_db)):
    try:
        return Psicologos.crear_psicologo(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    

@router.get("/psicologos/{id}", response_model=PsicologoResponse)
def obtener_psicologo(id: int, db: Session = Depends(get_db)):
    try:
        return Psicologos.obtener_psicologo_por_id(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

#-------------------------------------------------------------------
# Usuarios
#-------------------------------------------------------------------

@router.get("/usuarios", response_model=List[UsuarioResponse])
def get_usuarios(db: Session = Depends(get_db)):
    return Usuarios.listar_usuarios(db)

@router.post("/usuarios",response_model=UsuarioResponse)
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return Usuarios.crear_usuario(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/usuarios/{id}", response_model=UsuarioResponse)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    try:
        return Usuarios.obtener_usuario_por_id(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

#-------------------------------------------------------------------
# Citas
#-------------------------------------------------------------------

@router.post("/citas", response_model=CitasResponse)
def crear_cita(data: CitasCreate, db: Session = Depends(get_db)):
    try:
        return Citas.crear_cita(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/citas/{id}", response_model=CitasResponse)   
def obtener_cita(id: int, db: Session = Depends(get_db)):
    try:
        return Citas.obtener_cita_por_id(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/citas", response_model=List[CitasResponse])  
def listar_citas(db: Session = Depends(get_db)):
    return Citas.listar_citas(db)

@router.get("/numeros-emergencia/{localidad_id}", response_model=List[NumeroEmergenciaResponse])
def obtener_numeros_por_localidad(localidad_id: int, db: Session = Depends(get_db)):
    """Obtener números de emergencia de una localidad"""
    numeros = NumerosE.obtener_numero_emergencia_por_id(db, localidad_id)
    return numeros

@router.get("/localidades", response_model=List[dict])
def obtener_localidades(db: Session = Depends(get_db)):
    """Obtener todas las localidades disponibles (solo lectura)"""
    from Models.Models import Localidad
    localidades = db.query(Localidad).all()
    return [{"id": l.id, "nombre": l.nombre} for l in localidades]

@router.get("/numeros-emergencia/{usuario_id}")
def obtener_numeros_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        usuario = db.query(Usuarios).filter(Usuarios.id == usuario_id).first()    
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        numeros = NumerosE.obtener_por_usuario(db, usuario_id)
        return numeros
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.on_event("startup")
def startup():
    db = SessionLocal()
    db.close()