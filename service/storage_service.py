import logging
import uuid
from fastapi import UploadFile
from starlette.concurrency import run_in_threadpool
from Core.exception import CustomException
from Core.supabase_cliente import supabase, SUPABASE_BUCKET

logger = logging.getLogger(__name__)

MAX_BYTES = 2 * 1024 * 1024  # 2 MB
MIME_POR_EXT = {"jpg": "image/jpeg", "png": "image/png", "webp": "image/webp"}


def _detectar_extension(datos: bytes) -> str | None:
    """Identifica el tipo real por los primeros bytes (no confía en el nombre ni en el content-type)."""
    if datos.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if datos.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if datos[:4] == b"RIFF" and datos[8:12] == b"WEBP":
        return "webp"
    return None


class StorageService:
    @staticmethod
    async def subir_foto_psicologo(file: UploadFile, psicologo_id: int) -> str:
        contenido = await file.read(MAX_BYTES + 1)
        if not contenido:
            raise CustomException("El archivo está vacío.", 400)
        if len(contenido) > MAX_BYTES:
            raise CustomException("La imagen no puede pasar de 2 MB.", 413)

        ext = _detectar_extension(contenido)
        if not ext:
            raise CustomException("Formato de imagen no permitido. Usa JPG, PNG o WEBP.", 400)

        ruta = f"avatars/psicologo_{psicologo_id}_{uuid.uuid4().hex[:8]}.{ext}"
        try:
            await run_in_threadpool(
                lambda: supabase.storage.from_(SUPABASE_BUCKET).upload(
                    path=ruta,
                    file=contenido,
                    file_options={"content-type": MIME_POR_EXT[ext]},
                )
            )
        except Exception:
            logger.exception("Error al subir la imagen a Supabase")
            raise CustomException("No se pudo subir la imagen. Intenta de nuevo.", 502)

        return supabase.storage.from_(SUPABASE_BUCKET).get_public_url(ruta)