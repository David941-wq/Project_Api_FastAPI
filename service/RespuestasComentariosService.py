from service.RespuestaComentarioService import RespuestaComentarioService


class RespuestasComentariosService(RespuestaComentarioService):
    def create_respuesta_comentario(self, db, respuesta_data, usuario_actual):
        return self.crear_respuesta(db, respuesta_data, usuario_actual)
