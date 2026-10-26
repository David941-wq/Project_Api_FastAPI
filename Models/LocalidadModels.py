from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Core.database import Base


class Localidad(Base):
    __tablename__ = "Ubicaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False, unique=True, index=True)

    usuarios = relationship(
        "Usuario",
        back_populates="localidad",
        passive_deletes="all",
    )
    psicologos = relationship(
        "Psicologo",
        back_populates="localidad",
        passive_deletes="all",
    )
    numeros_emergencia = relationship(
        "NumeroEmergencia",
        back_populates="localidad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return f"<Localidad id={self.id} nombre={self.nombre}>"
