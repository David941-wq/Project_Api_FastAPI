from repositories.Usuario import UsuarioRepository
from repositories.localidad import LocalidadRepository
from Models.UserModels import Usuario
from Core.security import hash_password, verify_password, create_access_token
from Core.exception import CustomException


class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        self.localidad_repository = LocalidadRepository()

    def crear_usuario(self, db, usuario_data):
        if self.usuario_repository.obtener_por_correo(db, usuario_data.correo):
            raise CustomException("El correo electrónico ya está registrado", 409)

        localidad = self.localidad_repository.obtener_por_id(db, usuario_data.localidad_id)
        if not localidad:
            raise CustomException("La localidad especificada no existe", 404)

        nuevo_usuario = Usuario(
            nombre=usuario_data.nombre,
            correo=usuario_data.correo,
            password_hash=hash_password(usuario_data.contraseña),
            telefono=usuario_data.telefono,
            localidad_id=usuario_data.localidad_id
        )
        return self.usuario_repository.crear_usuario(db, nuevo_usuario)

    def listar_usuarios(self, db, solo_activos: bool = True):
        return self.usuario_repository.listar_usuarios(db, solo_activos)

    def obtener_usuario_por_id(self, db, usuario_id):
        usuario = self.usuario_repository.obtener_por_id(db, usuario_id)
        if not usuario:
            raise CustomException("Usuario no encontrado", 404)
        return usuario

    def login(self, db, datos):
        usuario = self.usuario_repository.obtener_por_correo(db, datos.correo)
        if not usuario or not verify_password(datos.contraseña, usuario.password_hash):
            raise CustomException("Credenciales inválidas", 401)

        token = create_access_token(data={"sub": str(usuario.id), "rol": "usuario"})
        return {
            "access_token": token,
            "token_type": "bearer",
            "usuario_id": usuario.id,
            "nombre": usuario.nombre
        }

    def cambiar_password(self, db, usuario_id, nueva_password_plana: str):
        usuario = self.obtener_usuario_por_id(db, usuario_id)
        nuevo_hash = hash_password(nueva_password_plana)
        return self.usuario_repository.actualizar_password(db, usuario.id, nuevo_hash)

    def desactivar_usuario(self, db, usuario_id):
        self.obtener_usuario_por_id(db, usuario_id)
        return self.usuario_repository.desactivar_usuario(db, usuario_id)
