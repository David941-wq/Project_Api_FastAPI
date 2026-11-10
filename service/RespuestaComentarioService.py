from repositories.RespuestaComentario import RespuestaComentarioRepository
from repositories.Comentario import ComentarioRepository
from repositories.Like import LikeRepository
from Models.LikeModels import RespuestaLike
from Models.RespuestasModels import RespuestaComentario
from Core.exception import CustomException


class RespuestaComentarioService:
    def __init__(self):
        self.respuesta_repository = RespuestaComentarioRepository()
        self.comentario_repository = ComentarioRepository()
        self.like_repository = LikeRepository(RespuestaLike, "respuesta_id")

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

    def listar_respuestas_con_likes(self, db, comentario_id, usuario_actual=None):
        respuestas = self.listar_respuestas_por_comentario(db, comentario_id)
        ids = [r.id for r in respuestas]
        conteos = self.like_repository.contar_por_ids(db, ids)
        mios = (
            self.like_repository.ids_con_like_de_usuario(db, usuario_actual.id, ids)
            if usuario_actual
            else set()
        )
        return [
            {
                "id": r.id,
                "contenido": r.contenido,
                "activo": r.activo,
                "comentario_id": r.comentario_id,
                "usuario_id": r.usuario_id,
                "created_at": r.created_at,
                "likes": conteos.get(r.id, 0),
                "liked": r.id in mios,
            }
            for r in respuestas
        ]

    def alternar_like(self, db, respuesta_id, usuario_actual):
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)
        if not respuesta.activo:
            raise CustomException("Respuesta no encontrada", 404)

        existente = self.like_repository.obtener(db, usuario_actual.id, respuesta_id)
        if existente:
            self.like_repository.eliminar(db, existente)
            liked = False
        else:
            self.like_repository.crear(db, usuario_actual.id, respuesta_id)
            liked = True

        return {
            "respuesta_id": respuesta_id,
            "likes": self.like_repository.contar(db, respuesta_id),
            "liked": liked,
        }

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
