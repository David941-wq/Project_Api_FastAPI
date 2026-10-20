from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Core.exception import CustomException
from API.router import router
from Core.database import engine, Base
from seed import populate_database

# Import all models to ensure SQLAlchemy registers them
# This is necessary before create_all() so that all relationships are resolved
from Models.UserModels import User
from Models.LocalidadModels import Localidad
from Models.NumeroEModels import NumeroEmergencia
from Models.PsicologosModels import Psicologo
from Models.CitasModels import Cita
from Models.ComentariosModels import Comentario
from Models.RespuestasModels import RespuestaComentario

Base.metadata.create_all(bind=engine)
populate_database()

#asda
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )

app.include_router(router)

# Inicio de la api
@app.get("/", tags=["Inicio"])
def inicio():
    return {"message": "Bienvenido a mi API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

