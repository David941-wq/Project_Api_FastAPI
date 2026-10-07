from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from Core.database import Base


class Psicologo(Base):
    __tablename__ = "psicologos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=True)
    correo = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    especialidad = Column(String(255), nullable=False, index=True)
    imagen = Column(String(255), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id", ondelete="RESTRICT"), nullable=False)
    localidad = relationship("Localidad", back_populates="psicologos")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    citas = relationship("Cita", back_populates="psicologo")

    def __repr__(self):
        return f"<Psicologo id={self.id} nombre={self.nombre} activo={self.activo}>"
