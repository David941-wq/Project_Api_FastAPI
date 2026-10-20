import enum
from sqlalchemy import (Column, Integer, Date, Time, Text, ForeignKey,UniqueConstraint, DateTime, Enum, func)
from sqlalchemy.orm import relationship
from Core.database import Base

class EstadoCita(str, enum.Enum):
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"


class Cita(Base):
    __tablename__ = "citas"
    __table_args__ = (UniqueConstraint('date', 'hour', name='unique_date_hour'),)
    #verifica si esta forma puede ser obtima y termina los modelos para proceder con el repository
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date, nullable=False, index=True)
    hour = Column(Time, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(EstadoCita), nullable=False, default=EstadoCita.PENDIENTE)

    psicologo_id = Column(Integer, ForeignKey("psicologos.id", ondelete="CASCADE"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # ondelete="CASCADE" para que si se elimina un psicologo o usuario, se eliminen sus citas asociadas

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # created_at → se llena automáticamente con la fecha/hora del servidor al crear el registro (server_default, calculado por la BD, no por Python — más confiable).
    # updated_at → se actualiza automáticamente cada vez que el registro se modifica (onupdate=func.now()).

    psicologo = relationship("Psicologo")
    usuario = relationship("User")

    def __repr__(self):
        return f"<Cita id={self.id} fecha={self.date} hora={self.hour} estado={self.status}>"
