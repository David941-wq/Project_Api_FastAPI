from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, UniqueConstraint
from Core.database import Base

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