from sqlalchemy.orm import Session
from Models.Models import Cita

class CitaRepository:
    def crear_cita(self, db: Session, cita: Cita):
        db.add(cita)
        db.commit()
        db.refresh(cita)

        return cita

    def listar_citas(self, db: Session):
        return db.query(Cita).all()
    
    def obtener_cita_por_id(self, db: Session, cita_id: int):
        return db.query(Cita).filter(Cita.id == cita_id).first()
    
    def obtener_cita_existente(self, db: Session, psicologo_id: int, fecha: str, hora: str):
        return db.query(Cita).filter(Cita.psicologo_id == psicologo_id, Cita.fecha == fecha, Cita.hora == hora).first()
    
    def obtener_citas_por_usuario(self, db: Session, usuario_id: int):
        return db.query(Cita).filter(Cita.usuario_id == usuario_id).all()
    
    