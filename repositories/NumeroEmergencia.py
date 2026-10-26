from sqlalchemy.orm import Session
from Models.NumeroEmergenciaModels import NumeroEmergencia


class NumeroEmergenciaRepository:

    def obtener_por_id(self, db: Session, numero_id: int) -> NumeroEmergencia | None:
        return db.query(NumeroEmergencia).filter(NumeroEmergencia.id == numero_id).first()

    def obtener_por_localidad(self, db: Session, localidad_id: int) -> list[NumeroEmergencia]:
        return (
            db.query(NumeroEmergencia)
            .filter(NumeroEmergencia.localidad_id == localidad_id)
            .all()
        )

    def listar_numeros_emergencia(self, db: Session) -> list[NumeroEmergencia]:
        return db.query(NumeroEmergencia).all()

    def crear_numero_emergencia(self, db: Session, numero: NumeroEmergencia) -> NumeroEmergencia:
        """Solo para el script de seed, no expuesto vía endpoint público."""
        db.add(numero)
        db.commit()
        db.refresh(numero)
        return numero
