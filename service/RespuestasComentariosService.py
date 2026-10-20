from repositories.RespuestaComentario import RespuestaComentarioRepository
from repositories.Comentarios import ComentarioRepository
from repositories.Usuario import UsuarioRepository
from Models.RespuestasModels import RespuestaComentario
from Core.exception import CustomException

class RespuestasComentariosService:
    def __init__(self):
        self.respuesta_comentario_repository = RespuestaComentarioRepository()
        self.comentario_repository = ComentarioRepository()
        self.usuario_repository = UsuarioRepository()

    def create_respuesta_comentario(self, respuesta: RespuestaComentario):
        # Check if the user exists
        usuario = self.usuario_repository.get_usuario_by_id(respuesta.usuario_id)
        if not usuario:
            raise CustomException("Usuario no encontrado", 404)

        # Check if the comentario exists
        comentario = self.comentario_repository.obtener_comentario_por_id(respuesta.comentario_id)
        if not comentario:
            raise CustomException("Comentario no encontrado", 404)

        nueva_respuesta = RespuestaComentario(
            contenido=respuesta.contenido,
            usuario_id=respuesta.usuario_id,
            comentario_id=respuesta.comentario_id
        )
        # Create the respuesta
        return self.respuesta_comentario_repository.create_respuesta_comentario(nueva_respuesta)

    def obtener_respuesta_por_id(self, db, respuesta_id: int):
        respuesta = self.respuesta_comentario_repository.obtener_respuesta_por_id(db, respuesta_id)
        if not respuesta:
            raise CustomException("Respuesta no encontrada", 404)
        return respuesta

    def actualizar_respuesta(self, db, respuesta_id: int, contenido: str):
        respuesta = self.respuesta_comentario_repository.obtener_respuesta_por_id(db, respuesta_id)
        if not respuesta:
            raise CustomException("Respuesta no encontrada", 404)
        return self.respuesta_comentario_repository.actualizar_respuesta(db, respuesta_id, contenido)

    def desactivar_respuesta(self, db, respuesta_id: int, usuario_id: int):
        respuesta = self.respuesta_comentario_repository.obtener_respuesta_por_id(db, respuesta_id)
        if not respuesta:
            raise CustomException("Respuesta no encontrada", 404)
        if respuesta.usuario_id != usuario_id:
            raise CustomException("No tienes autorización para eliminar esta respuesta", 403)
        
        return self.respuesta_comentario_repository.desactivar_respuesta(db, respuesta_id)
