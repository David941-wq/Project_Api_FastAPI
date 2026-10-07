from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from Core.database import Base


class Comentario(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contenido = Column(Text, nullable=False)
    activo = Column(Boolean, nullable=False, default=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    usuario = relationship("Usuario", back_populates="comentarios")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    respuestas = relationship(
        "RespuestaComentario",
        back_populates="comentario",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Comentario id={self.id} usuario_id={self.usuario_id}>"
