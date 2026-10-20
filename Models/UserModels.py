from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True,index=True)
    hashed_password = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    is_activate = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    localidad_id = Column(Integer, ForeignKey("Ubicaciones.id", ondelete="RESTRICT"), nullable=False)
    localidad = relationship("Localidad")

    comentarios = relationship("Comentario", cascade="all, delete-orphan")
    respuestas = relationship("RespuestaComentario", cascade="all, delete-orphan")

    citas = relationship("Cita")



# class Usuario(Base):
#     __tablename__ = "usuarios"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
#     nombre = Column(String(255), nullable=False)
#     correo = Column(String(255), nullable=False)
#     contraseña = Column(String(255), nullable=False)
#     ubicacion = Column(String(255), nullable=False)
#     telefono = Column(String(255), nullable=False)

#     localidad_id = Column(Integer, ForeignKey("Ubicaciones.id"))

#     localidad = relationship("Localidad",back_populates="usuarios")

#     citas = relationship("Cita", back_populates="usuario")