from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.router import router
from Core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# Inicio de la api
@app.get("/", tags=["Inicio"])
def inicio():
    return {"message": "Bienvenido a mi API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

