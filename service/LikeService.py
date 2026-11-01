from repositories.Like import LikeRepository
from repositories.Comentario import ComentarioRepository
from Core.exception import CustomException


class LikeService:
    def __init__(self):
        self.like_repository = LikeRepository()
        self.comentario_repository = ComentarioRepository()

    def alternar_like(self, db, comentario_id, usuario_actual):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, comentario_id)
        if not comentario or not comentario.activo:
            raise CustomException("Comentario no encontrado", 404)

        existente = self.like_repository.obtener(db, usuario_actual.id, comentario_id)
        if existente:
            self.like_repository.eliminar(db, existente)
            liked = False
        else:
            self.like_repository.crear(db, usuario_actual.id, comentario_id)
            liked = True

        return {
            "comentario_id": comentario_id,
            "likes": self.like_repository.contar(db, comentario_id),
            "liked": liked,
        }