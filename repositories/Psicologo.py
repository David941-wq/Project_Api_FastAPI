from sqlalchemy.orm import Session
from Models.PsicologosModels import Psicologo


class PsicologoRepository:

    def crear_psicologo(self, db: Session, psicologo: Psicologo) -> Psicologo:
        """Recibe un objeto Psicologo con password_hash YA aplicado (hasheado en el service)."""
        db.add(psicologo)
        db.commit()
        db.refresh(psicologo)
        return psicologo

    def obtener_psicologo_por_id(self, db: Session, psicologo_id: int) -> Psicologo | None:
        return db.query(Psicologo).filter(Psicologo.id == psicologo_id).first()

    def obtener_psicologo_por_correo(self, db: Session, correo: str) -> Psicologo | None:
        return db.query(Psicologo).filter(Psicologo.correo == correo).first()

    def listar_psicologos(self, db: Session, solo_activos: bool = True) -> list[Psicologo]:
        query = db.query(Psicologo)
        if solo_activos:
            query = query.filter(Psicologo.activo == True)
        return query.all()

    def obtener_por_localidad(self, db: Session, localidad_id: int) -> list[Psicologo]:
        return (
            db.query(Psicologo)
            .filter(Psicologo.localidad_id == localidad_id, Psicologo.activo == True)
            .all()
        )

    def obtener_por_especialidad(self, db: Session, especialidad: str) -> list[Psicologo]:
        return (
            db.query(Psicologo)
            .filter(Psicologo.especialidad.ilike(f"%{especialidad}%"), Psicologo.activo == True)
            .all()
        )

    def actualizar_psicologo(self, db: Session, psicologo_id: int, datos: dict) -> Psicologo | None:
        psicologo = self.obtener_psicologo_por_id(db, psicologo_id)
        if not psicologo:
            return None
        for campo, valor in datos.items():
            setattr(psicologo, campo, valor)
        db.commit()
        db.refresh(psicologo)
        return psicologo

    def actualizar_password(self, db: Session, psicologo_id: int, password_hash: str) -> Psicologo | None:
        psicologo = self.obtener_psicologo_por_id(db, psicologo_id)
        if psicologo:
            psicologo.password_hash = password_hash
            db.commit()
            db.refresh(psicologo)
        return psicologo

    def desactivar_psicologo(self, db: Session, psicologo_id: int) -> Psicologo | None:
        psicologo = self.obtener_psicologo_por_id(db, psicologo_id)
        if psicologo:
            psicologo.activo = False
            db.commit()
            db.refresh(psicologo)
        return psicologo
