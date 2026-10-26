from repositories.RespuestaComentario import RespuestaComentarioRepository
from repositories.Comentario import ComentarioRepository
from Models.RespuestasModels import RespuestaComentario
from Core.exception import CustomException


class RespuestaComentarioService:
    def __init__(self):
        self.respuesta_repository = RespuestaComentarioRepository()
        self.comentario_repository = ComentarioRepository()

    def crear_respuesta(self, db, respuesta_data, usuario_actual):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, respuesta_data.comentario_id)
        if not comentario:
            raise CustomException("El comentario no existe", 404)

        nueva_respuesta = RespuestaComentario(
            contenido=respuesta_data.contenido,
            comentario_id=respuesta_data.comentario_id,
            usuario_id=usuario_actual.id
        )
        return self.respuesta_repository.crear_respuesta(db, nueva_respuesta)

    def obtener_respuesta_por_id(self, db, respuesta_id):
        respuesta = self.respuesta_repository.obtener_respuesta_por_id(db, respuesta_id)
        if not respuesta:
            raise CustomException("Respuesta no encontrada", 404)
        return respuesta

    def listar_respuestas_por_comentario(self, db, comentario_id):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, comentario_id)
        if not comentario:
            raise CustomException("El comentario no existe", 404)
        return self.respuesta_repository.listar_respuestas_por_comentario(db, comentario_id)

    def actualizar_respuesta(self, db, respuesta_id, usuario_actual, nuevo_contenido: str):
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)

        if respuesta.usuario_id != usuario_actual.id:
            raise CustomException("No tienes permiso para editar esta respuesta", 403)

        return self.respuesta_repository.actualizar_respuesta(db, respuesta_id, nuevo_contenido)

    def desactivar_respuesta(self, db, respuesta_id, usuario_actual):
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)

        if respuesta.usuario_id != usuario_actual.id:
            raise CustomException("No tienes permiso para eliminar esta respuesta", 403)

        return self.respuesta_repository.desactivar_respuesta(db, respuesta_id)
