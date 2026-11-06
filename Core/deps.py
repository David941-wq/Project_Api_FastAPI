from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from Core.security import decode_access_token
from Core.exception import CustomException
from Core.database import get_db
from repositories.Usuario import UsuarioRepository
from repositories.Psicologo import PsicologoRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
oauth2_opcional = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_access_token(token)
    except ValueError:
        raise CustomException("Token inválido o expirado", 401)

    usuario_id = payload.get("sub")
    rol = payload.get("rol")
    if usuario_id is None or rol != "usuario":
        raise CustomException("Token inválido", 401)

    usuario_repo = UsuarioRepository()
    usuario = usuario_repo.obtener_por_id(db, int(usuario_id))
    if not usuario:
        raise CustomException("Usuario no encontrado", 404)
    return usuario


def obtener_psicologo_actual(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_access_token(token)
    except ValueError:
        raise CustomException("Token inválido o expirado", 401)

    psicologo_id = payload.get("sub")
    rol = payload.get("rol")
    if psicologo_id is None or rol != "psicologo":
        raise CustomException("Token inválido", 401)

    psicologo_repo = PsicologoRepository()
    psicologo = psicologo_repo.obtener_psicologo_por_id(db, int(psicologo_id))
    if not psicologo:
        raise CustomException("Psicólogo no encontrado", 404)
    return psicologo

def obtener_usuario_opcional(token: str | None = Depends(oauth2_opcional), db=Depends(get_db)):
    """Devuelve el usuario si llega un token válido; si no, None (visitante)."""
    if not token:
        return None
    try:
        payload = decode_access_token(token)
    except ValueError:
        return None

    if payload.get("rol") != "usuario" or payload.get("sub") is None:
        return None
    return UsuarioRepository().obtener_por_id(db, int(payload["sub"]))

def obtener_cuenta_autenticada(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_access_token(token)
    except ValueError:
        raise CustomException("Token inválido o expirado", 401)

    cuenta_id = payload.get("sub")
    rol = payload.get("rol")
    if cuenta_id is None:
        raise CustomException("Token inválido", 401)

    if rol == "usuario":
        cuenta = UsuarioRepository().obtener_por_correo(db, int(cuenta_id))
    elif rol == "psicologo":
        cuenta = PsicologoRepository().obtener_psicologo_por_id(db, int(cuenta_id))
    else:
        raise CustomException("Token invalido", 401)

    if not cuenta:
        raise CustomException("Cuenta no encontrada", 404)
    return cuenta