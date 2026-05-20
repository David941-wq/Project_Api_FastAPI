from sqlalchemy.orm import Session
from Models.Models import Localidad


class LocalidadRepository:

    def crear_localidad(self, db: Session, datos: Localidad):
        db.add(datos)
        db.commit()
        db.refresh(datos)
        return datos

    def obtener_localidad(self, db: Session, id: int):
        return db.query(Localidad).filter(Localidad.id == id).first()

    def listar_localidades(self, db: Session):
        return db.query(Localidad).all()