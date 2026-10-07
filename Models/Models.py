# Punto central de import: garantiza que todos los modelos se registren
# en el Base de SQLAlchemy antes de resolver relationships(), y sirve
# como import corto para otros archivos (ej: seed.py).

from Models.LocalidadModels import Localidad
from Models.NumeroEmergenciaModels import NumeroEmergencia
from Models.UserModels import Usuario
from Models.PsicologosModels import Psicologo
from Models.CitasModels import Cita, EstadoCita
from Models.ComentariosModels import Comentario
from Models.RespuestasModels import RespuestaComentario

__all__ = [
    "Localidad",
    "NumeroEmergencia",
    "Usuario",
    "Psicologo",
    "Cita",
    "EstadoCita",
    "Comentario",
    "RespuestaComentario",
]
