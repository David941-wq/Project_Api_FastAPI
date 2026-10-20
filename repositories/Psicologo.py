from sqlalchemy.orm import Session
from Models.PsicologosModels import Psicologo

dataPsicologo = Psicologo

class PsicologoRepository:

    def crear_psicologo(self, db: Session, psicologo: dataPsicologo) -> dataPsicologo:
        db.add(psicologo)
        db.commit()
        db.refresh(psicologo)
        return psicologo


    def obtener_psicologo_por_id(self, db: Session, psicologo_id: int) -> dataPsicologo | None:
        return db.query(dataPsicologo).filter(dataPsicologo.id == psicologo_id).first()
    
    def obtener_psicologo_por_correo(self, db: Session, correo: str) -> dataPsicologo | None:
        return db.query(dataPsicologo).filter(dataPsicologo.correo == correo).first()

    def listar_psicologos(self, db: Session) -> list[dataPsicologo]:
        return db.query(dataPsicologo).all()

    def obtener_por_localidad(self, db: Session, localidad: str) -> list[dataPsicologo]:
        return db.query(dataPsicologo).filter(dataPsicologo.localidad == localidad).all()

    def obtener_por_especialidad(self, db: Session, especialidad: str) -> list[dataPsicologo]:
        return db.query(dataPsicologo).filter(dataPsicologo.especiality.ilike(f"%{especialidad}%"), dataPsicologo.status == True).all()

    def actualizar_psicologo(self, db: Session, psicologo_id: int, datos: dict) -> dataPsicologo | None:
        psicologo = self.obtener_psicologo_por_id(db, psicologo_id)
        if not psicologo:
            return None
        for campo, valor in datos.items():
            setattr(psicologo, campo, valor)
        db.commit()
        db.refresh(psicologo)
        return psicologo

    def actualizar_password(self, db: Session, psicologo_id: int, nueva_contrasena: str) -> dataPsicologo | None:
        psicologo = self.obtener_psicologo_por_id(db, psicologo_id)
        if not psicologo:
            return None
        psicologo.contrasena = nueva_contrasena
        db.commit()
        db.refresh(psicologo)
        return psicologo

    def desactivar_psicologo(self, db: Session, psicologo_id: int) -> dataPsicologo | None:
        psicologo = self.obtener_psicologo_por_id(db, psicologo_id)
        if not psicologo:
            return None
        psicologo.status = False
        db.commit()
        db.refresh(psicologo)
        return psicologo