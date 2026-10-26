from sqlalchemy.orm import Session
from Models.CitasModels import Cita, EstadoCita


class CitaRepository:

    def crear_cita(self, db: Session, cita: Cita) -> Cita:
        db.add(cita)
        db.commit()
        db.refresh(cita)
        return cita

    def obtener_por_id(self, db: Session, cita_id: int) -> Cita | None:
        return db.query(Cita).filter(Cita.id == cita_id).first()

    def obtener_por_usuario_id(self, db: Session, usuario_id: int) -> list[Cita]:
        return db.query(Cita).filter(Cita.usuario_id == usuario_id).all()

    def obtener_por_psicologo_id(self, db: Session, psicologo_id: int) -> list[Cita]:
        return db.query(Cita).filter(Cita.psicologo_id == psicologo_id).all()

    def obtener_cita_existente(self, db: Session, psicologo_id: int, date, hour) -> Cita | None:
        return (
            db.query(Cita)
            .filter(
                Cita.psicologo_id == psicologo_id,
                Cita.date == date,
                Cita.hour == hour,
                Cita.status != EstadoCita.CANCELADA
            )
            .first()
        )

    def cambiar_fecha(self, db: Session, cita_id: int, nueva_fecha, nueva_hora=None) -> Cita | None:
        cita = self.obtener_por_id(db, cita_id)
        if cita:
            cita.date = nueva_fecha
            if nueva_hora:
                cita.hour = nueva_hora
            db.commit()
            db.refresh(cita)
        return cita

    def cambiar_estado(self, db: Session, cita_id: int, nuevo_estado: EstadoCita) -> Cita | None:
        cita = self.obtener_por_id(db, cita_id)
        if cita:
            cita.status = nuevo_estado
            db.commit()
            db.refresh(cita)
        return cita

    def cancelar_cita(self, db: Session, cita_id: int) -> Cita | None:
        return self.cambiar_estado(db, cita_id, EstadoCita.CANCELADA)
