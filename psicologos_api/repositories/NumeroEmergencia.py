from sqlalchemy.orm import Session
from Models.Models import NumeroEmergencia, Usuario


class NumeroEmergenciaRepository:

    def crear_numero(self, db: Session, datos: NumeroEmergencia):
        db.add(datos)
        db.commit()
        db.refresh(datos)
        return datos

    def obtener_por_localidad_id(self, db: Session, localidad_id: int):

        return (
            db.query(NumeroEmergencia)
            .filter(NumeroEmergencia.localidad_id == localidad_id)
            .all()
        )
    
    def obtener_por_usuario(self, db: Session, usuario_id: int):
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

        if not usuario:
            return []
        
        return (
            db.query(NumeroEmergencia).filter(NumeroEmergencia.localidad_id == usuario.localidad_id).all()
        )
    