from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from Core.database import Base


class RespuestaComentario(Base):
    __tablename__ = "respuestas_comentarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contenido = Column(Text, nullable=False)
    activo = Column(Boolean, nullable=False, default=True)

    comentario_id = Column(Integer, ForeignKey("comentarios.id", ondelete="CASCADE"), nullable=False, index=True)
    comentario = relationship("Comentario", back_populates="respuestas")

    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    usuario = relationship("Usuario", back_populates="respuestas")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<RespuestaComentario id={self.id} comentario_id={self.comentario_id}>"
