from sqlalchemy.orm import Session
from Models.LocalidadModels import Localidad

DataLocalidad = Localidad

class LocalidadRepository:

    def obtener_localidad(self, db: Session, id: int) -> DataLocalidad | None:
        return db.query(DataLocalidad).filter(DataLocalidad.id == id).first()

    def obtener_por_nombre(self, db: Session, nombre: str) -> DataLocalidad | None:
        return db.query(DataLocalidad).filter(DataLocalidad.nombre == nombre).first()

    def listar_localidades(self, db: Session) -> list[DataLocalidad]:
        return db.query(DataLocalidad).all()

    def obtener_con_numeros_emergencia(self, db: Session, localidad_id: int) -> DataLocalidad | None:
        return db.query(DataLocalidad).filter(DataLocalidad.id == localidad_id).first()

    def crear_localidad(self, db: Session, localidad: DataLocalidad) -> DataLocalidad:
        db.add(localidad)
        db.commit()
        db.refresh(localidad)
        return localidad

    