from Core.exception import CustomException
from Core.security import verify_password
from repositories.Usuario import UsuarioRepository
from repositories.Psicologo import PsicologoRepository
from service.UsuarioService import UsuarioService
from service.PsicologoService import PsicologoService


class AuthService:
    """Un solo login para usuarios y psicólogos."""

    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        self.psicologo_repository = PsicologoRepository()
        self.usuario_service = UsuarioService()
        self.psicologo_service = PsicologoService()

    def login(self, db, datos):
        # 1) cuenta de usuario
        usuario = self.usuario_repository.obtener_por_correo(db, datos.correo)
        if usuario and verify_password(datos.password, usuario.password_hash):
            return self.usuario_service.login(db, datos)

        # 2) cuenta de psicólogo
        psicologo = self.psicologo_repository.obtener_psicologo_por_correo(db, datos.correo)
        if psicologo and verify_password(datos.password, psicologo.password_hash):
            return self.psicologo_service.login(db, datos)

        # mismo mensaje en todos los fallos: no revela si el correo existe ni en qué tabla
        raise CustomException("Credenciales inválidas", 401)