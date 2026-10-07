from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Core.exception import CustomException
from API.router import router
from Core.database import engine, Base
from seed import populate_database

Base.metadata.create_all(bind=engine)
populate_database()

app = FastAPI(title="API Psicólogos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {"message": "Bienvenido a mi API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
