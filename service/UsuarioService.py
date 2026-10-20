from repositories.Usuario import UsuarioRepository
from repositories.localidad import LocalidadRepository
from Models.UserModels import User
from Core.security import hash_password, VerifyPassword, create_access_token
from Core.exception import CustomException

class UsuarioService:
    def __init__(self):
        self.usuario_repositorio = UsuarioRepository()
        self.localidad_repositorio = LocalidadRepository()

    def crear_usuario(self, db, usuario_data):
        # Verificar si el correo ya existe
        existentes = self.usuario_repositorio.obtener_por_correo(db, usuario_data.correo)
        if existentes:
            raise CustomException("Ya existe un usuario con ese correo", 400)

        # Verificar si la localidad existe
        localidad = self.localidad_repositorio.obtener_localidad(db, usuario_data.localidad_id)
        if not localidad:
            raise CustomException("La localidad especificada no existe", 400)

        nuevo_usuario = User(
            nombre = usuario_data.nombre,
            correo = usuario_data.correo,
            password = hash_password(usuario_data.password),
            localidad_id = usuario_data.localidad_id,
            imagen = usuario_data.imagen,
        )
        return self.usuario_repositorio.crear_usuario(db, nuevo_usuario)

    def listar_usuarios(self, db, solo_activos= True):
        return self.usuario_repositorio.listar_usuarios(db, solo_activos)

    def obtener_usuario_por_id(self, db, usuario_id):
        usuario = self.usuario_repositorio.obtener_usuario_por_id(db, usuario_id)
        if not usuario or not VerifyPassword():
            raise CustomException("Usuario no encontrado", 404)
        return usuario #llegaste a actualizar login
    

    def login(self, db, datos):
        usuario = self.usuario_repositorio.obtener_por_correo(db, datos.correoh)
        if not usuario or not VerifyPassword(datos.contraseña, usuario.password_has):
            raise CustomException("Usuario valido", 401)
        
        token = create_access_token(data={"sub": str(usuario.id), "rol": "usuario"})
        return {"acces_token": token, "token_type": "bearer", "usuario": usuario}

    def actualizar_usuario(self, db, usuario_id, usuario_data):
        usuario = self.usuario_repositorio.obtener_por_id(db, usuario_id)
        if not usuario:
            raise CustomException("Usuario no encontrado", 404)

        # Verificar si la localidad existe
        localidad = self.localidad_repositorio.obtener_localidad(db, usuario_data.localidad_id)
        if not localidad:
            raise CustomException("La localidad especificada no existe", 400)

        usuario.nombre = usuario_data.nombre
        usuario.correo = usuario_data.correo
        if usuario_data.password:
            usuario.password = hash_password(usuario_data.password)
        usuario.localidad_id = usuario_data.localidad_id
        usuario.imagen = usuario_data.imagen

        return self.usuario_repositorio.actualizar_usuario(db, usuario)

    def desactivar_usuario(self, db, usuario_id):
        usuario = self.usuario_repositorio.obtener_por_id(db, usuario_id)
        if not usuario:
            raise CustomException("Usuario no encontrado", 404)

        usuario.activo = False
        return self.usuario_repositorio.actualizar_usuario(db, usuario)