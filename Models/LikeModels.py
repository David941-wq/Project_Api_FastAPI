from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint, func
from Core.database import Base

class ComentarioLike(Base):
    __tablename__ = "comentario_like"
    __table_args__ = (
        UniqueConstraint("usuario_id", "comentario_id", name = "uq_like_usuario_comentario"),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    comentario_id = Column(Integer, ForeignKey("comentarios.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<ComentariosLike usuario_id={self.usuario_id} comentario_id={self.comentario_id}>"


class RespuestaLike(Base):
    """Un registro por cada usuario que dio like a una respuesta."""
    __tablename__ = "respuesta_like"
    __table_args__ = (
        UniqueConstraint("usuario_id", "respuesta_id", name="uq_like_usuario_respuesta"),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    respuesta_id = Column(Integer, ForeignKey("respuestas_comentarios.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<RespuestaLike usuario_id={self.usuario_id} respuesta_id={self.respuesta_id}>"