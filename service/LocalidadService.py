from repositories.localidad import LocalidadRepository
from Core.exception import CustomException


class LocalidadService:
    def __init__(self):
        self.localidad_repository = LocalidadRepository()

    def listar_localidades(self, db):
        return self.localidad_repository.listar_localidades(db)

    def obtener_localidad_por_id(self, db, localidad_id):
        localidad = self.localidad_repository.obtener_por_id(db, localidad_id)
        if not localidad:
            raise CustomException("Localidad no encontrada", 404)
        return localidad
