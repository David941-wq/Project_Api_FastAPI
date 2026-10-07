from sqlalchemy.orm import Session, joinedload
from Models.LocalidadModels import Localidad


class LocalidadRepository:

    def obtener_por_id(self, db: Session, localidad_id: int) -> Localidad | None:
        return db.query(Localidad).filter(Localidad.id == localidad_id).first()

    def obtener_por_nombre(self, db: Session, nombre: str) -> Localidad | None:
        return db.query(Localidad).filter(Localidad.nombre == nombre).first()

    def listar_localidades(self, db: Session) -> list[Localidad]:
        return db.query(Localidad).all()

    def obtener_con_numeros_emergencia(self, db: Session, localidad_id: int) -> Localidad | None:
        return (
            db.query(Localidad)
            .options(joinedload(Localidad.numeros_emergencia))
            .filter(Localidad.id == localidad_id)
            .first()
        )

    def crear_localidad(self, db: Session, localidad: Localidad) -> Localidad:
        """Solo para el script de seed, no expuesto vía endpoint público."""
        db.add(localidad)
        db.commit()
        db.refresh(localidad)
        return localidad
