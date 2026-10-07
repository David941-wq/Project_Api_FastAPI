from sqlalchemy.orm import Session
from Models.RespuestasModels import RespuestaComentario


class RespuestaComentarioRepository:

    def crear_respuesta(self, db: Session, respuesta: RespuestaComentario) -> RespuestaComentario:
        db.add(respuesta)
        db.commit()
        db.refresh(respuesta)
        return respuesta

    def obtener_respuesta_por_id(self, db: Session, respuesta_id: int) -> RespuestaComentario | None:
        return db.query(RespuestaComentario).filter(RespuestaComentario.id == respuesta_id).first()

    def listar_respuestas_por_comentario(self, db: Session, comentario_id: int) -> list[RespuestaComentario]:
        return (
            db.query(RespuestaComentario)
            .filter(RespuestaComentario.comentario_id == comentario_id, RespuestaComentario.activo == True)
            .order_by(RespuestaComentario.created_at.asc())
            .all()
        )

    def actualizar_respuesta(self, db: Session, respuesta_id: int, contenido: str) -> RespuestaComentario | None:
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)
        if respuesta:
            respuesta.contenido = contenido
            db.commit()
            db.refresh(respuesta)
        return respuesta

    def desactivar_respuesta(self, db: Session, respuesta_id: int) -> RespuestaComentario | None:
        respuesta = self.obtener_respuesta_por_id(db, respuesta_id)
        if respuesta:
            respuesta.activo = False
            db.commit()
            db.refresh(respuesta)
        return respuesta
