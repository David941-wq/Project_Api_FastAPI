from sqlalchemy.orm import Session
from Models.RespuestasModels import RespuestaComentario

dataRespuestaComentario = RespuestaComentario

class RespuestaComentarioRepository:

    def crear_respuesta(self, db: Session, respuesta: dataRespuestaComentario) -> dataRespuestaComentario:
        db.add(respuesta)
        db.commit()
        db.refresh(respuesta)
        return respuesta

    def obtener_respuesta_por_id(self, db: Session, respuesta_id: int) -> dataRespuestaComentario | None:
        return db.query(dataRespuestaComentario).filter(dataRespuestaComentario.id == respuesta_id).first()

    def listar_respuestas_por_comentario(self, db: Session, comentario_id: int) -> list[dataRespuestaComentario]:
        return (db.query(dataRespuestaComentario).filter(dataRespuestaComentario.comentario_id == comentario_id, dataRespuestaComentario.is_active == True)
                .order_by(dataRespuestaComentario.created_at.asc()).all())

    def actualizar_respuesta(self, db: Session, respuesta_id: int, contenido: str) -> dataRespuestaComentario | None:
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)
        if respuesta:
            respuesta.contenido = contenido
            db.commit()
            db.refresh(respuesta)
        return respuesta

    def desactivar_respuesta(self, db: Session, respuesta_id: int) -> dataRespuestaComentario | None:
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)
        if respuesta:
            respuesta.is_active = False
            db.commit()
            db.refresh(respuesta)
        return respuesta

    # terminaste los repo sigue con los services y
    # los controller para las request

    