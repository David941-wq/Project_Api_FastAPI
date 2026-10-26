from repositories.Comentario import ComentarioRepository
from Models.ComentariosModels import Comentario
from Core.exception import CustomException


class ComentarioService:
    def __init__(self):
        self.comentario_repository = ComentarioRepository()

    def crear_comentario(self, db, comentario_data, usuario_actual):
        nuevo_comentario = Comentario(
            contenido=comentario_data.contenido,
            usuario_id=usuario_actual.id
        )
        return self.comentario_repository.crear_comentario(db, nuevo_comentario)

    def listar_comentarios(self, db, solo_activos: bool = True):
        return self.comentario_repository.listar_comentarios(db, solo_activos)

    def obtener_comentario_por_id(self, db, comentario_id):
        comentario = self.comentario_repository.obtener_comentario_por_id(db, comentario_id)
        if not comentario:
            raise CustomException("Comentario no encontrado", 404)
        return comentario

    def obtener_comentario_con_respuestas(self, db, comentario_id):
        comentario = self.comentario_repository.obtener_con_respuestas(db, comentario_id)
        if not comentario:
            raise CustomException("Comentario no encontrado", 404)
        return comentario

    def listar_mis_comentarios(self, db, usuario_actual):
        return self.comentario_repository.obtener_comentarios_por_usuario(db, usuario_actual.id)

    def actualizar_comentario(self, db, comentario_id, usuario_actual, nuevo_contenido: str):
        comentario = self.obtener_comentario_por_id(db, comentario_id)

        if comentario.usuario_id != usuario_actual.id:
            raise CustomException("No tienes permiso para editar este comentario", 403)

        return self.comentario_repository.actualizar_comentario(db, comentario_id, nuevo_contenido)

    def desactivar_comentario(self, db, comentario_id, usuario_actual):
        comentario = self.obtener_comentario_por_id(db, comentario_id)

        if comentario.usuario_id != usuario_actual.id:
            raise CustomException("No tienes permiso para eliminar este comentario", 403)

        return self.comentario_repository.desactivar_comentario(db, comentario_id)
