from sqlalchemy.orm import Session
from Models.Models import Usuario
from Models.Models import Cita

class UsuarioRepository:
    def crear_usuario(self, db: Session, datos: Usuario):
        db.add(datos)
        db.commit()
        db.refresh(datos)
        return datos

    def obtener_usuario(self, db: Session, id: int):
        return db.query(Usuario).filter(Usuario.id == id).first()

    def obtener_por_correo(self, db: Session, correo: str):
        return db.query(Usuario).filter(Usuario.correo == correo).first()
    
    def obtener_usuario_por_id(self, db: Session, usuario_id: int):
        return db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def listar_usuarios(self, db: Session):
        return db.query(Usuario).all()
    
    def login(self, db, nombre, contraseña):
        return db.query(Usuario).filter(Usuario.nombre == nombre, Usuario.contraseña == contraseña).first()

    def eliminar_usuario(self, db: Session, id: int):
        usuario = db.query(Usuario).filter(Usuario.id == id).first()

        if usuario:
            db.delete(usuario)
            db.commit()

        return usuario
    
    def obtener_citas_por_usuario_id(self, db: Session, usuario_id: int):
        return db.query(Cita).filter(Cita.usuario_id == usuario_id).all()
    
    def Cambiar_fecha_cita(self, db: Session, cita_id: int, nueva_fecha):
        cita = db.query(Cita).filter(Cita.id == cita_id).first()
        if cita:
            cita.fecha = nueva_fecha
            db.commit()
            db.refresh(cita)
        return cita
    
    def cancelar_cita(self, db: Session, cita_id: int):
        cita = db.query(Cita).filter(Cita.id == cita_id).first()
        if cita:
            db.delete(cita)
            db.commit()
        return cita