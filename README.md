<<<<<<< HEAD
# Project_Api_FastAPI
Desarrollo del api personal
=======
# Project_Api_FastApi

## Instalación

1. Crear y activar entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate      (Windows)
   source venv/bin/activate   (Linux/Mac)
   ```

2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Crear el archivo `.env` en la raíz del proyecto (mismo nivel que `main.py`),
   usando como base `.env.example`. El contenido real te lo compartieron aparte
   en el chat — no lo subas a git.

4. Asegúrate de tener PostgreSQL corriendo y de que `DATABASE_URL` en tu `.env`
   apunte a una base de datos existente (créala antes si no existe, ej:
   `createdb nombre_de_tu_bd` o desde pgAdmin).

5. Ejecutar la API:
   ```
   uvicorn main:app --reload
   ```
   o
   ```
   python main.py
   ```

6. Documentación interactiva disponible en:
   ```
   http://localhost:8000/docs
   ```

## Notas

- Al arrancar, la API crea automáticamente las tablas (`Base.metadata.create_all`)
  y puebla `localidades` + `numeros_emergencia` si están vacías (`seed.py`).
- Los endpoints de citas, comentarios, respuestas y "mis números de emergencia"
  requieren autenticación: primero `POST /login` (usuario) o `POST /psicologos/login`
  (psicólogo), y usar el `access_token` devuelto como `Authorization: Bearer <token>`.
>>>>>>> 66ebbe6 (primer commit)
