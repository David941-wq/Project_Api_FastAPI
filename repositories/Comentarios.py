from sqlalchemy.orm import Session, joinedload
from Models.ComentariosModels import Comentario

dataComentario = Comentario

class ComentarioRepository:

    def crear_comentario(self, db: Session, comentario: dataComentario) -> dataComentario:
        db.add(comentario)
        db.commit()
        db.refresh(comentario)
        return comentario

    def obtener_comentario_por_id(self, db: Session, comentario_id: int) -> dataComentario | None:
        return db.query(dataComentario).filter(dataComentario.id == comentario_id).first()

    def obtener_con_respuesta(self, db: Session, comentario_id: int) -> dataComentario | None:
        return (db.query(dataComentario).options(joinedload(dataComentario.respuesta)).filter(dataComentario.id == comentario_id).first())

    def listar_comentarios(self, db: Session, solo_activos: bool = True) -> list[dataComentario]:
        query = db.query(dataComentario)
        if solo_activos:
            query = query.filter(dataComentario.is_active == True)
        return query.order_by(dataComentario.created_at.desc()).all()

    def obtener_comentarios_por_usuario(self, db: Session, usuario_id: int) -> list[dataComentario]:
        return db.query(dataComentario).filter(dataComentario.usuario_id == usuario_id, dataComentario.is_active == True).all()

    def actualizar_comentario(self, db: Session, comentario_id: int, contenido: str) -> dataComentario | None:
        comentario = self.obtener_comentario_por_id(db, comentario_id)
        if comentario:
            comentario.contenido = contenido
            db.commit()
            db.refresh(comentario)
        return comentario

    def desactivar_comentario(self, db: Session, comentario_id: int) -> dataComentario | None:
        comentario = self.obtener_comentario_por_id(db, comentario_id)
        if comentario:
            comentario.is_active = False
            db.commit()
            db.refresh(comentario)
        return comentario
