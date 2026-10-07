from repositories.Psicologo import PsicologoRepository
from repositories.localidad import LocalidadRepository
from repositories.Citas import CitaRepository
from Models.PsicologosModels import Psicologo
from Core.security import hash_password, verify_password, create_access_token
from Core.exception import CustomException


class PsicologoService:
    def __init__(self):
        self.psicologo_repository = PsicologoRepository()
        self.localidad_repository = LocalidadRepository()
        self.cita_repository = CitaRepository()

    def crear_psicologo(self, db, psicologo_data):
        existentes = self.psicologo_repository.obtener_psicologo_por_correo(db, psicologo_data.correo)
        if existentes:
            raise CustomException("Ya existe un psicólogo con ese correo", 409)

        localidad = self.localidad_repository.obtener_por_id(db, psicologo_data.localidad_id)
        if not localidad:
            raise CustomException("La localidad especificada no existe", 404)

        nuevo_psicologo = Psicologo(
            nombre=psicologo_data.nombre,
            descripcion=psicologo_data.descripcion,
            correo=psicologo_data.correo,
            password_hash=hash_password(psicologo_data.contraseña),
            localidad_id=psicologo_data.localidad_id,
            especialidad=psicologo_data.especialidad,
            imagen=psicologo_data.imagen,
        )
        return self.psicologo_repository.crear_psicologo(db, nuevo_psicologo)

    def listar_psicologos(self, db, solo_activos: bool = True):
        return self.psicologo_repository.listar_psicologos(db, solo_activos)

    def obtener_psicologo_por_id(self, db, psicologo_id):
        psicologo = self.psicologo_repository.obtener_psicologo_por_id(db, psicologo_id)
        if not psicologo:
            raise CustomException("Psicólogo no encontrado", 404)
        return psicologo

    def listar_por_localidad(self, db, localidad_id):
        return self.psicologo_repository.obtener_por_localidad(db, localidad_id)

    def listar_por_especialidad(self, db, especialidad: str):
        return self.psicologo_repository.obtener_por_especialidad(db, especialidad)

    def login(self, db, datos):
        psicologo = self.psicologo_repository.obtener_psicologo_por_correo(db, datos.correo)
        if not psicologo or not verify_password(datos.contraseña, psicologo.password_hash):
            raise CustomException("Credenciales inválidas", 401)

        token = create_access_token(data={"sub": str(psicologo.id), "rol": "psicologo"})
        return {
            "access_token": token,
            "token_type": "bearer",
            "psicologo_id": psicologo.id,
            "nombre": psicologo.nombre
        }

    def desactivar_psicologo(self, db, psicologo_id):
        self.obtener_psicologo_por_id(db, psicologo_id)
        return self.psicologo_repository.desactivar_psicologo(db, psicologo_id)
