from sqlalchemy.orm import Session, joinedload
from Models.ComentariosModels import Comentario


class ComentarioRepository:

    def crear_comentario(self, db: Session, comentario: Comentario) -> Comentario:
        db.add(comentario)
        db.commit()
        db.refresh(comentario)
        return comentario

    def obtener_comentario_por_id(self, db: Session, comentario_id: int) -> Comentario | None:
        return db.query(Comentario).filter(Comentario.id == comentario_id).first()

    def obtener_con_respuestas(self, db: Session, comentario_id: int) -> Comentario | None:
        return (
            db.query(Comentario)
            .options(joinedload(Comentario.respuestas))
            .filter(Comentario.id == comentario_id)
            .first()
        )

    def listar_comentarios(self, db: Session, solo_activos: bool = True) -> list[Comentario]:
        query = db.query(Comentario)
        if solo_activos:
            query = query.filter(Comentario.activo == True)
        return query.order_by(Comentario.created_at.desc()).all()

    def obtener_comentarios_por_usuario(self, db: Session, usuario_id: int) -> list[Comentario]:
        return (
            db.query(Comentario)
            .filter(Comentario.usuario_id == usuario_id, Comentario.activo == True)
            .all()
        )

    def actualizar_comentario(self, db: Session, comentario_id: int, contenido: str) -> Comentario | None:
        comentario = self.obtener_comentario_por_id(db, comentario_id)
        if comentario:
            comentario.contenido = contenido
            db.commit()
            db.refresh(comentario)
        return comentario

    def desactivar_comentario(self, db: Session, comentario_id: int) -> Comentario | None:
        comentario = self.obtener_comentario_por_id(db, comentario_id)
        if comentario:
            comentario.activo = False
            db.commit()
            db.refresh(comentario)
        return comentario
