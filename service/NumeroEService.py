from repositories.NumeroEmergencia import NumeroEmergenciaRepository
from Core.exception import CustomException

class NumeroEService:
    def __init__(self):
        self.numero_emergencia_repository = NumeroEmergenciaRepository()

    def listar_numeros_emergencia(self, db, solo_activos=True):
        return self.numero_emergencia_repository.listar_numeros_emergencia(db, solo_activos)

    def obtener_por_localidad(self, db, localidad_id):
        numeros = self.numero_emergencia_repository.obtener_numeros_emergencia_por_localidad(db, localidad_id)
        if not numeros:
            raise CustomException("No se encontraron números de emergencia para la localidad especificada", 404)
        return numeros

    def obtener_mis_numeros_emergencia(self, db, usuario_actual):
        return self.numero_emergencia_repository.obtener_numeros_emergencia_por_usuario(db, usuario_actual.id)
    