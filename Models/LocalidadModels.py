from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Core.database import Base


class Localidad(Base):
    __tablename__ = "Ubicaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    users = relationship("User", lazy='select')
    psicologos = relationship("Psicologo", lazy='select')
    numeros_emergencia = relationship("NumeroEmergencia", lazy='select')

    def __repr__(self):
        return f"<Localidad id={self.id} name={self.name}>"