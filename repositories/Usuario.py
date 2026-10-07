from sqlalchemy.orm import Session
from Models.UserModels import Usuario


class UsuarioRepository:

    def crear_usuario(self, db: Session, usuario: Usuario) -> Usuario:
        """Recibe un objeto Usuario con password_hash YA aplicado (hasheado en el service)."""
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario

    def obtener_por_id(self, db: Session, usuario_id: int) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def obtener_por_correo(self, db: Session, correo: str) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.correo == correo).first()

    def listar_usuarios(self, db: Session, solo_activos: bool = True) -> list[Usuario]:
        query = db.query(Usuario)
        if solo_activos:
            query = query.filter(Usuario.activo == True)
        return query.all()

    def actualizar_usuario(self, db: Session, usuario_id: int, datos: dict) -> Usuario | None:
        usuario = self.obtener_por_id(db, usuario_id)
        if not usuario:
            return None
        for campo, valor in datos.items():
            setattr(usuario, campo, valor)
        db.commit()
        db.refresh(usuario)
        return usuario

    def actualizar_password(self, db: Session, usuario_id: int, password_hash: str) -> Usuario | None:
        usuario = self.obtener_por_id(db, usuario_id)
        if usuario:
            usuario.password_hash = password_hash
            db.commit()
            db.refresh(usuario)
        return usuario

    def desactivar_usuario(self, db: Session, usuario_id: int) -> Usuario | None:
        usuario = self.obtener_por_id(db, usuario_id)
        if usuario:
            usuario.activo = False
            db.commit()
            db.refresh(usuario)
        return usuario

    def eliminar_usuario_permanente(self, db: Session, usuario_id: int) -> Usuario | None:
        """Borrado físico real. Usar con cuidado (ej: solo para GDPR / derecho al olvido)."""
        usuario = self.obtener_por_id(db, usuario_id)
        if usuario:
            db.delete(usuario)
            db.commit()
        return usuario
