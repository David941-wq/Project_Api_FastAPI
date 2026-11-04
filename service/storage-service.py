import os
import uuid
from fastapi import UploadFile
from Core.exception import CustomException
from Core.supabase_cliente import supabase, SUPABASE_BUCKET

BUCKET_NAME = os.getenv("SUPABASE_BUCKET", SUPABASE_BUCKET)

class StorageService:
    @staticmethod
    async def upload_psicologo_photo(file: UploadFile, psicologo_id: int):
        ext = file.filename.split(".")[-1].lower()
        if ext not in ["jpg", "jpeg", "png", "webp"]:
            raise CustomException(status_code=400, message="Formato de imagen no permitido. Usa JPG, PNG o WEBP.")

        file_path = f"avatars/psicologo_{psicologo_id}_{uuid.uuid4().hex[:6]}.{ext}"
        content = await file.read()

        try:
            supabase.storage.from_(BUCKET_NAME).upload(
                path=file_path,
                file=content,
                file_options={"content-type": file.content_type, "upsert": "true"}
            )
        except Exception as e:
            raise CustomException(
                status_code=500,
                message=f"Error al subir la imagen: {str(e)}"
            )
        return supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)