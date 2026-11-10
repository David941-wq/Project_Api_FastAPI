from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Models.LikeModels import ComentarioLike, RespuestaLike


class LikeRepository:
    """Likes de comentarios (por defecto) o de respuestas:
        LikeRepository()                              -> comentarios
        LikeRepository(RespuestaLike, "respuesta_id") -> respuestas
    """

    def __init__(self, modelo=ComentarioLike, campo: str = "comentario_id"):
        self.modelo = modelo
        self.campo = getattr(modelo, campo)  # la columna: ComentarioLike.comentario_id o RespuestaLike.respuesta_id

    def obtener(self, db: Session, usuario_id: int, objeto_id: int):
        return (
            db.query(self.modelo)
            .filter(self.modelo.usuario_id == usuario_id, self.campo == objeto_id)
            .first()
        )

    def crear(self, db: Session, usuario_id: int, objeto_id: int) -> None:
        db.add(self.modelo(**{"usuario_id": usuario_id, self.campo.key: objeto_id}))
        try:
            db.commit()
        except IntegrityError:
            # doble clic rápido: el like ya existía, no es un error
            db.rollback()

    def eliminar(self, db: Session, like) -> None:
        db.delete(like)
        db.commit()

    def contar(self, db: Session, objeto_id: int) -> int:
        return (
            db.query(func.count(self.modelo.id))
            .filter(self.campo == objeto_id)
            .scalar()
            or 0
        )

    def contar_por_ids(self, db: Session, ids: list[int]) -> dict[int, int]:
        if not ids:
            return {}
        filas = (
            db.query(self.campo, func.count(self.modelo.id))
            .filter(self.campo.in_(ids))
            .group_by(self.campo)
            .all()
        )
        return {objeto_id: total for objeto_id, total in filas}

    # nombre anterior: se conserva para no tocar ComentarioService
    contar_por_comentarios = contar_por_ids

    def ids_con_like_de_usuario(self, db: Session, usuario_id: int, ids: list[int]) -> set[int]:
        if not ids:
            return set()
        filas = (
            db.query(self.campo)
            .filter(self.modelo.usuario_id == usuario_id, self.campo.in_(ids))
            .all()
        )
        return {fila[0] for fila in filas}