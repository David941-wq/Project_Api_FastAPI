from sqlalchemy.orm import Session
from Models.Models import Psicologo
from Models.Models import Cita


class PsicologoRepository:

    def crear_psicologo(self, db: Session, data):
        psicologo = Psicologo(**data.dict())
        db.add(psicologo)
        db.commit()
        db.refresh(psicologo)

        return psicologo

    def get_psicologos(self, db: Session):
        return db.query(Psicologo).all()

    def get_psicologo_by_id(self, psicologo_id: int, db: Session):
        return db.query(Psicologo).filter(Psicologo.id == psicologo_id).first()
    
    def get_citas_by_psicologo_id(self, db: Session, psicologo_id: int):
        return db.query(Cita).filter(Cita.psicologo_id == psicologo_id).all()
    
    def posponer_cita(db: Session, cita_id: int, nueva_fecha):
        cita = db.query(Cita).filter(Cita.id == cita_id).first()
        if cita:
            cita.fecha = nueva_fecha
            db.commit()
            db.refresh(cita)
        return cita
    def obtener_psicologo_por_correo(self, db: Session, correo: str):
        return db.query(Psicologo).filter(Psicologo.correo == correo).first()