from repositories.Psicologo import PsicologoRepository
from repositories.localidad import LocalidadRepository
from Models.PsicologosModels import Psicologo
from Core.security import hash_password
from Core.exception import CustomException

class PsicologoService:
    def __init__(self):
        self.psicologo_repository = PsicologoRepository()
        self.localidad_repository = LocalidadRepository()

    def crear_psicologo(self, db, psicologo_data):
        # Verificar si el correo ya existe
        existentes = self.psicologo_repository.obtener_psicologo_por_correo(db, psicologo_data.correo)
        if existentes:
            raise CustomException("Ya existe un psicólogo con ese correo", 400)

        # Verificar si la localidad existe
        localidad = self.localidad_repository.obtener_localidad_por_id(db, psicologo_data.localidad_id)
        if not localidad:
            raise CustomException("La localidad especificada no existe", 400)

        nuevo_psicologo = Psicologo(
            nombre = psicologo_data.nombre,
            descripcion = psicologo_data.descripcion,
            correo = psicologo_data.correo,
            password = hash_password(psicologo_data.password),
            localidad_id = psicologo_data.localidad_id,
            especialidad = psicologo_data.especialidad,
            imagen = psicologo_data.imagen,
        )
        return self.psicologo_repository.crear_psicologo(db, nuevo_psicologo)

    def listar_psicologos(self, db, solo_activos=True):
        return self.psicologo_repository.listar_psicologos(db, solo_activos)

    def obtener_psicologo_por_id(self, db, psicologo_actual):
        psicologo = self.psicologo_repository.obtener_psicologo_por_id(db, psicologo_actual.id)
        if not psicologo:
            raise CustomException("Psicólogo no encontrado", 404)
        return psicologo

    def listar_mis_psicologos(self, db, usuario_actual):
        return self.psicologo_repository.listar_psicologos_por_usuario(db, usuario_actual.id)