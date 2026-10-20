from sqlalchemy.orm import Session
from Models.NumeroEModels import NumeroEmergencia

dataNumeroEmergencia = NumeroEmergencia

class NumeroEmergenciaRepository:

    def obtener_por_id(self, db: Session, numero_id: int) -> dataNumeroEmergencia | None:
        return db.query(dataNumeroEmergencia).filter(dataNumeroEmergencia.id == numero_id).first()

    def obtener_por_localidad(self, db: Session, localidad: str) -> list[dataNumeroEmergencia]:
        return db.query(dataNumeroEmergencia).filter(dataNumeroEmergencia.localidad == localidad).all()

    def crear_numero_emergencia(self, db: Session, numero: dataNumeroEmergencia) -> dataNumeroEmergencia:
        db.add(numero)
        db.commit()
        db.refresh(numero)
        return numero