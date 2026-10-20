from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Core.database import Base

class NumeroEmergencia(Base):
    __tablename__ = "numeros_emergencia"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)   # ej: "Policía", "Bomberos", "Línea de crisis"
    numero = Column(String(20), nullable=False)

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id"))
    localidad = relationship("Localidad")

    def __repr__(self):
        return f"<NumeroEmergencia id={self.id} nombre={self.nombre} numero={self.numero}>"

#tabla no debe de tener registros para ingresarse solo sirve para coneccion con la tabla de 
# localidades y numeros de emergencia