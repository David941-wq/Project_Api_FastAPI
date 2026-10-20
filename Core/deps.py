from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from Core.security import decode_access_token
from Core.exception import CustomException
from Core.database import get_db  
from repositories.Usuario import UsuarioRepository
from repositories.Psicologo import PsicologoRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
usuario_repo = UsuarioRepository()
psicologo_repo = PsicologoRepository()

def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_access_token(token)
        usuario_id = payload.get("sub")
        rol = payload.get("rol")
        if usuario_id is None or rol != "usuario":
            raise CustomException("Token inválido", 401)
    except JWTError:
        raise CustomException("Token inválido o expirado", 401)

    usuario = usuario_repo.obtener_por_id(db,int(usuario_id))
    if not usuario:
        raise CustomException("Usuario no encontrado", 404)
    return usuario

def obtener_psicologo_actual(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_access_token(token)
        psicologo_id = payload.get("sub")
        rol = payload.get("rol")
        if psicologo_id is None or rol != "psicologo":
            raise CustomException("Token inválido", 401)
    except JWTError:
        raise CustomException("Token inválido o expirado", 401)

    psicologo = usuario_repo.obtener_por_id(db,int(psicologo_id))
    if not psicologo:
        raise CustomException("Psicologo no encontrado", 404)
    return psicologo