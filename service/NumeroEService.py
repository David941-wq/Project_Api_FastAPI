from repositories.NumeroEmergencia import NumeroEmergenciaRepository
from Core.exception import CustomException


class NumeroEService:
    def __init__(self):
        self.numero_emergencia_repository = NumeroEmergenciaRepository()

    def listar_numeros_emergencia(self, db):
        return self.numero_emergencia_repository.listar_numeros_emergencia(db)

    def obtener_por_localidad(self, db, localidad_id):
        numeros = self.numero_emergencia_repository.obtener_por_localidad(db, localidad_id)
        if not numeros:
            raise CustomException("No hay números de emergencia para esta localidad", 404)
        return numeros

    def obtener_mis_numeros_emergencia(self, db, usuario_actual):
        """usuario_actual ya viene resuelto desde el token, con su localidad_id incluido."""
        return self.numero_emergencia_repository.obtener_por_localidad(db, usuario_actual.localidad_id)
