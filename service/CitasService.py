from repositories.Citas import CitaRepository
from repositories.Psicologo import PsicologoRepository
from Models.CitasModels import Cita
from Core.exception import CustomException


class CitasService:
    def __init__(self):
        self.cita_repository = CitaRepository()
        self.psicologo_repository = PsicologoRepository()

    def crear_cita(self, db, cita_data, usuario_actual):
        if not self.psicologo_repository.obtener_psicologo_por_id(db, cita_data.psicologo_id):
            raise CustomException("Psicólogo no encontrado", 404)

        existe = self.cita_repository.obtener_cita_existente(
            db, cita_data.psicologo_id, cita_data.date, cita_data.hour
        )
        if existe:
            raise CustomException(
                "Ya existe una cita para este psicólogo en la fecha y hora especificadas", 409
            )

        nueva_cita = Cita(
            date=cita_data.date,
            hour=cita_data.hour,
            usuario_id=usuario_actual.id,
            psicologo_id=cita_data.psicologo_id,
            description=getattr(cita_data, 'description', None)
        )
        return self.cita_repository.crear_cita(db, nueva_cita)

    def listar_por_psicologo(self, db, psicologo_actual):
        return self.cita_repository.obtener_por_psicologo_id(db, psicologo_actual.id)

    def listar_mis_citas(self, db, usuario_actual):
        return self.cita_repository.obtener_por_usuario_id(db, usuario_actual.id)

    def obtener_cita_por_id(self, db, cita_id):
        cita = self.cita_repository.obtener_por_id(db, cita_id)
        if not cita:
            raise CustomException("Cita no encontrada", 404)
        return cita

    def cancelar_cita(self, db, cita_id, usuario_actual):
        cita = self.obtener_cita_por_id(db, cita_id)

        if cita.usuario_id != usuario_actual.id:
            raise CustomException("No tienes permiso para cancelar esta cita", 403)

        return self.cita_repository.cancelar_cita(db, cita_id)

    def cambiar_fecha_hora(self, db, cita_id, nueva_fecha, nueva_hora, usuario_actual):
        cita = self.obtener_cita_por_id(db, cita_id)

        if cita.usuario_id != usuario_actual.id:
            raise CustomException("No tienes permiso para cambiar la fecha y hora de esta cita", 403)

        return self.cita_repository.cambiar_fecha(db, cita_id, nueva_fecha, nueva_hora)
