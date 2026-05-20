from sqlalchemy import Column, Integer, String, Date,Time, ForeignKey
from sqlalchemy.orm import relationship
from Core.database import Base


class Psicologo(Base):
    __tablename__ = "psicologos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255),nullable=False)
    descripcion = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False)
    contraseña = Column(String(255), nullable=False)
    ubicacion = Column(String(255), nullable=False)
    especialidad = Column(String(255), nullable=False)
    imagen = Column(String(255), nullable=False)

    citas = relationship("Cita", back_populates="psicologo")

#---------------------------

# usuario_localidad = Table(
#     "usuario_localidad",
#     Base.metadata,
#     Column("usuario_id", Integer, ForeignKey("usuarios.id")),
#     Column("localidad_id", Integer, ForeignKey("Ubicaciones.id"))
# )

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False)
    contraseña = Column(String(255), nullable=False)
    ubicacion = Column(String(255), nullable=False)
    telefono = Column(String(255), nullable=False)

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id"))

    localidad = relationship("Localidad",back_populates="usuarios")

    citas = relationship("Cita", back_populates="usuario")

class Localidad(Base):
    __tablename__ = "Ubicaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)

    usuarios = relationship("Usuario", back_populates="localidad")
    numeros_emergencia = relationship("NumeroEmergencia", back_populates="localidad")

    
class NumeroEmergencia(Base):
    __tablename__ = "Numeros_emergencia"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero = Column(Integer, nullable=False)

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id"))
    localidad = relationship("Localidad",back_populates="numeros_emergencia"
    )
    
    
class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    psicologo_id = Column(Integer, ForeignKey("psicologos.id"))
    
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)

    usuario = relationship("Usuario", back_populates="citas")

    psicologo = relationship("Psicologo", back_populates="citas")