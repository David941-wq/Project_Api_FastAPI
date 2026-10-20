from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from Core.database import Base


class Psicologo(Base):
    __tablename__ = "psicologos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    especiality = Column(String(255), nullable=False, index=True)
    imagen = Column(String(255), nullable=True)
    status = Column(Boolean, nullable=False, default=True)

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id", ondelete="RESTRICT"), nullable=False)
    localidad = relationship("Localidad")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    citas = relationship("Cita")

    def __repr__(self):
        return f"<Psicologo id={self.id} name={self.name} status={self.status}>"