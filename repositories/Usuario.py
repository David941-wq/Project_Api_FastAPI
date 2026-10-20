from sqlalchemy.orm import Session
from Models.UserModels import User
from typing import List

dateUse = User

class UsuarioRepository:
    def crear_usuario(self, db: Session, datos: dateUse) -> dateUse:
        db.add(datos)
        db.commit()
        db.refresh(datos)
        return datos

    def obtener_por_id(self, db: Session, id: int) -> dateUse:
        return db.query(dateUse).filter(dateUse.id == id).first()

    def obtener_por_correo(self, db: Session, correo: str):
        return db.query(dateUse).filter(dateUse.email == correo).first()
    
    def listar_usuarios(self, db: Session, activos: bool = True) -> List[dateUse]:
        query = db.query(dateUse)
        if activos:
            query = query.filter(dateUse.is_activate == True)
        return query.all()

    def actualizar_usuario(self, db: Session, user_id: int, datos: dict) -> dateUse | None:
        usuario = self.obtener_por_id(db, user_id)
        if not usuario:
            return None
        for campo, valor in datos.items():
            setattr(usuario, campo, valor)
        db.commit()
        db.refresh(usuario)
        return usuario

    def desactivar_usuario(self, db: Session, user_id: int) -> dateUse | None:
        usuario = self.obtener_por_id(db, user_id)
        if not usuario:
            return None
        usuario.is_activate = False
        db.commit()
        db.refresh(usuario)
        return usuario

    def eliminar_usuario(self, db: Session, user_id: int) -> dateUse | None:
        usuario = self.obtener_por_id(db, user_id)
        if usuario:
            db.delete(usuario)
            db.commit()
        return usuario
    