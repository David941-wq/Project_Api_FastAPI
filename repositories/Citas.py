from sqlalchemy.orm import Session
from Models.CitasModels import Cita

dataCita = Cita

class CitaRepository:

    def crear_cita(self, db: Session, cita: dataCita) -> dataCita:
        db.add(cita)
        db.commit()
        db.refresh(cita)
        return cita

    def obtener_cita_por_id(self, db: Session, cita_id: int) -> dataCita | None:
        return db.query(dataCita).filter(dataCita.id == cita_id).first()
    
    def obtener_cita_por_usuario(self, db: Session, usuario_id: int) -> list[dataCita]:
        return db.query(dataCita).filter(dataCita.usuario_id == usuario_id).all()

    def obtener_cita_psicologo(self, db: Session, psi_id: int) -> list[dataCita]:
        return db.query(dataCita).filter(dataCita.psicologo_id == psi_id).all()

    def obtener_cita_existente(self, db: Session, psicologo_id: int, date, hour) -> Cita | None:
        return (
            db.query(Cita)
            .filter(
                Cita.psicologo_id == psicologo_id,
                Cita.date == date,
                Cita.hour == hour,
                Cita.status != Cita.EstadoCita.CANCELADA
            )
            .first()
        )

    def cambiar_fecha(self, db: Session, cita_id: int, nueva_fecha: str) -> dataCita | None:
        cita = db.query(dataCita).filter(dataCita.id == cita_id).first()
        if cita:
            cita.date = nueva_fecha
            db.commit()
            db.refresh(cita)
        return cita

    def cancelar_cita(self, db: Session, cita_id: int) -> Cita | None:
        return self.cambiar_estado(db, cita_id, "cancelada")