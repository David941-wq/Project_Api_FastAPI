import enum
from sqlalchemy import (
    Column, Integer, Date, Time, Text, ForeignKey,
    UniqueConstraint, DateTime, Enum, func
)
from sqlalchemy.orm import relationship
from Core.database import Base


class EstadoCita(str, enum.Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"


class Cita(Base):
    __tablename__ = "citas"
    __table_args__ = (
        UniqueConstraint('psicologo_id', 'date', 'hour', name='unique_psicologo_date_hour'),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date, nullable=False, index=True)
    hour = Column(Time, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(EstadoCita), nullable=False, default=EstadoCita.PENDIENTE)

    psicologo_id = Column(Integer, ForeignKey("psicologos.id", ondelete="CASCADE"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    psicologo = relationship("Psicologo", back_populates="citas")
    usuario = relationship("Usuario", back_populates="citas")

    def __repr__(self):
        return f"<Cita id={self.id} fecha={self.date} hora={self.hour} estado={self.status}>"
