from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Models.LikeModels import ComentarioLike


class LikeRepository:

    def obtener(self, db: Session, usuario_id: int, comentario_id: int) -> ComentarioLike | None:
        return (
            db.query(ComentarioLike)
            .filter(
                ComentarioLike.usuario_id == usuario_id,
                ComentarioLike.comentario_id == comentario_id,
            )
            .first()
        )

    def crear(self, db: Session, usuario_id: int, comentario_id: int) -> None:
        db.add(ComentarioLike(usuario_id=usuario_id, comentario_id=comentario_id))
        try:
            db.commit()
        except IntegrityError:
            # doble clic rápido: el like ya existía, no es un error
            db.rollback()

    def eliminar(self, db: Session, like: ComentarioLike) -> None:
        db.delete(like)
        db.commit()

    def contar(self, db: Session, comentario_id: int) -> int:
        return (
            db.query(func.count(ComentarioLike.id))
            .filter(ComentarioLike.comentario_id == comentario_id)
            .scalar()
            or 0
        )

    def contar_por_comentarios(self, db: Session, ids: list[int]) -> dict[int, int]:
        if not ids:
            return {}
        filas = (
            db.query(ComentarioLike.comentario_id, func.count(ComentarioLike.id))
            .filter(ComentarioLike.comentario_id.in_(ids))
            .group_by(ComentarioLike.comentario_id)
            .all()
        )
        return {comentario_id: total for comentario_id, total in filas}

    def ids_con_like_de_usuario(self, db: Session, usuario_id: int, ids: list[int]) -> set[int]:
        if not ids:
            return set()
        filas = (
            db.query(ComentarioLike.comentario_id)
            .filter(
                ComentarioLike.usuario_id == usuario_id,
                ComentarioLike.comentario_id.in_(ids),
            )
            .all()
        )
        return {fila[0] for fila in filas}