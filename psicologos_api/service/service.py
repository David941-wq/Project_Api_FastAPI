from repositories.Psicologo import PsicologoRepository
from repositories.Usuario import UsuarioRepository
from repositories.localidad import LocalidadRepository
from repositories.NumeroEmergencia import NumeroEmergenciaRepository
from repositories.Citas import CitaRepository
from Models.Models import Usuario, Psicologo, Cita, NumeroEmergencia, Localidad

class PsicologoService:
    def __init__(self):
        self.psicologo_repository = PsicologoRepository()

    def crear_psicologo(self,db, psicologo_data):
        existentes = self.psicologo_repository.obtener_psicologo_por_correo(db, psicologo_data.correo)
        if existentes:
            raise ValueError("Ya existe un psicólogo con ese correo")
        
        # nuevo_psicologo = Psicologo(
        #     nombre=psicologo_data.nombre,
        #     descripcion=psicologo_data.descripcion,
        #     correo=psicologo_data.correo,
        #     contraseña=psicologo_data.contraseña,
        #     ubicacion=psicologo_data.ubicacion,
        #     especialidad=psicologo_data.especialidad,
        #     imagen=psicologo_data.imagen
        # )
        
        return self.psicologo_repository.crear_psicologo(db, psicologo_data)
    
    def Listar_psicologos(self, db):
        return self.psicologo_repository.listar_psicologos(db)
    
    def obtener_psicologo_por_id(self, db, psicologo_id):
        psicologo = self.psicologo_repository.obtener_psicologo_by_id(db, psicologo_id)
        if not psicologo:
            raise ValueError("Psicólogo no encontrado")
        return psicologo

    def listar_usuarios_por_correo(self, db, correo):
        return [u for u in self.usuario_repository.obtener_usuario(db) if u.correo == correo]
    
    def Listar_citas_por_psicologo(self, db, psicologo_id):
        return self.cita_repository.obtener_citas_por_psicologo(db, psicologo_id)
    
class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def crear_usuario(self, db, usuario_data):
        existente = self.usuario_repository.obtener_por_correo(db, usuario_data.correo)
        if existente:
            raise ValueError("El correo electrónico ya está registrado")
        
        nuevo_usuario = Usuario(
            nombre=usuario_data.nombre,
            correo=usuario_data.correo,
            contraseña=usuario_data.contraseña,
            ubicacion=usuario_data.ubicacion,
            telefono=usuario_data.telefono,
            localidad_id=usuario_data.localidad_id
        )
        
        return self.usuario_repository.crear_usuario(db, nuevo_usuario)
    
    def listar_usuarios(self, db):
        return self.usuario_repository.listar_usuarios(db)
    
    def obtener_usuario_por_id(self, db, usuario_id):
        usuario = self.usuario_repository.obtener_usuario_por_id(db, usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        return usuario
    
    def validar_correo(self, db, correo):
        existente = self.usuario_repository.obtener_por_correo(db, correo)
        if existente:
            return True
        return False
    
    def login(self, db, datos):
        usuario = self.usuario_repository.login(
            db,
            datos.nombre,
            datos.contraseña
        )
        if not usuario:
            raise ValueError(
                "Credenciales inválidas"
            )

        return usuario
    
    
class NumeroEmergenciaService:
    def __init__(self):
        self.numero_emergencia_repository = NumeroEmergenciaRepository()

    def listar_numeros_emergencia(self, db):
        return self.numero_emergencia_repository.obtener_numeros_emergencia(db)
    
    def obtener_numero_emergencia_por_id(self, db, localidad_id):
        numero = self.numero_emergencia_repository.obtener_por_localidad_id(db, localidad_id)
        if not numero:
            raise ValueError("Número de emergencia no encontrado")
        return numero
    
    def obtener_numero_emergencia_por_usuario(self, db, usuario_id):
        numeros = self.numero_emergencia_repository.obtener_por_usuario(db, usuario_id)
        if not numeros:
            raise ValueError("No se encontraron números de emergencia para el usuario")
        return numeros
    
class CitasService:
    def __init__(self):
        self.cita_repository = CitaRepository()

    def crear_cita(self, db, cita_data):
        existente = self.cita_repository.obtener_cita_existente(db,cita_data.psicologo_id,cita_data.fecha,cita_data.hora)
        if existente:
            raise ValueError("Ya existe una cita programada para esta fecha y hora\nProfavor ingrese otra fecha y hora")
        
        nueva_cita = Cita(
            usuario_id=cita_data.usuario_id,
            psicologo_id=cita_data.psicologo_id,
            fecha=cita_data.fecha,
            hora=cita_data.hora
        )

        return self.cita_repository.crear_cita(db, nueva_cita)
    
    
    def obtener_cita_por_id(self, db, cita_id):
        cita = self.cita_repository.obtener_cita_por_id(db, cita_id)
        if not cita:
            raise ValueError("Cita no encontrada")
        return cita
    
    def listar_citas(self, db):
        return self.cita_repository.listar_citas(db)
    