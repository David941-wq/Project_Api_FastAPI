from repositories.Comentarios import ComentarioRepository
from repositories.Usuario import UsuarioRepository
from Models.ComentariosModels import Comentario
from Core.exception import CustomException

class ComentariosService:
    def __init__(self):
        self.comentario_repository = ComentarioRepository()
        self.usuario_repository = UsuarioRepository()

    def create_comentario(self, comentario: Comentario):
        # Check if the user exists
        usuario = self.usuario_repository.get_usuario_by_id(comentario.usuario_id)
        if not usuario:
            raise CustomException("Usuario no encontrado", 404)

        nuevo_comentario = Comentario(
            contenido=comentario.contenido,
            usuario_id=comentario.usuario_id
        )
        # Create the comentario
        return self.comentario_repository.create_comentario(nuevo_comentario)

    def listar_comentarios(self, db, solo_activos: bool = True):
        return self.comentario_repository.listar_comentarios(db, solo_activos)

    def obtener_comentario_por_id(self, db, comentario_id: int):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, comentario_id)
        if not comentario:
            raise CustomException("Comentario no encontrado", 404)
        return comentario

    def obtener_comentario_con_respuesta(self, db, comentario_id: int):
        comentario = self.comentario_repository.obtener_con_respuesta(db, comentario_id)
        if not comentario:
            raise CustomException("Comentario no encontrado", 404)
        return comentario

    def listar_comentarios_por_usuario(self, db, usuario_id: int):
        usuario = self.usuario_repository.get_usuario_by_id(usuario_id)
        if not usuario:
            raise CustomException("Usuario no encontrado", 404)
        return self.comentario_repository.obtener_comentarios_por_usuario(db, usuario_id)

    def actualizar_comentario(self, db, comentario_id: int, usuario_actual, nuevo_contenido: str):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, comentario_id)
        if comentario.usuario_id != usuario_actual.id:
            raise CustomException("No tienes autorización para actualizar este comentario", 403)
        return self.comentario_repository.actualizar_comentario(db, comentario_id, nuevo_contenido)

    def desactivar_comentario(self, db, comentario_id: int, usuario_id: int):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, comentario_id)
        if comentario.usuario_id != usuario_id:
            raise CustomException("No tienes autorización para eliminar este comentario", 403)

        return self.comentario_repository.desactivar_comentario(db, comentario_id)