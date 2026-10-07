from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from Core.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id", ondelete="RESTRICT"), nullable=False)
    localidad = relationship("Localidad", back_populates="usuarios")

    citas = relationship("Cita", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    respuestas = relationship("RespuestaComentario", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario id={self.id} nombre={self.nombre} activo={self.activo}>"
