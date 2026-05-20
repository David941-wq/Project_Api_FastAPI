from Core.database import SessionLocal, engine, Base
from Models.Models import Localidad, NumeroEmergencia

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Limpiar datos existentes (opcional)
db.query(NumeroEmergencia).delete()
db.query(Localidad).delete()

# Insertar países/localidades
paises = [
    {"nombre": "Colombia", "numeros": [112, 119, 123]},
    {"nombre": "Argentina", "numeros": [911, 107]},
    {"nombre": "México", "numeros": [911, 66]},
    {"nombre": "España", "numeros": [112, 91, 62]},
    {"nombre": "Chile", "numeros": [131, 133, 138]},
    {"nombre": "Perú", "numeros": [105, 106]},
    {"nombre": "Brasil", "numeros": [190, 192, 193]},
    {"nombre": "Estados Unidos", "numeros": [911]},
    {"nombre": "Canadá", "numeros": [911]},
    {"nombre": "Francia", "numeros": [112, 15, 17]},
    {"nombre": "Alemania", "numeros": [110, 112]},
    {"nombre": "Reino Unido", "numeros": [999, 112]},
    {"nombre": "Italia", "numeros": [112, 113]},
    {"nombre": "Australia", "numeros": [000]},
    {"nombre": "Japón", "numeros": [110, 119]},
]

# Crear localidades y sus números de emergencia
for pais in paises:
    # Crear la localidad
    localidad = Localidad(nombre=pais["nombre"])
    db.add(localidad)
    db.commit()
    
    # Agregar números de emergencia
    for numero in pais["numeros"]:
        num_emergencia = NumeroEmergencia(numero=numero, localidad_id=localidad.id)
        db.add(num_emergencia)
    
    db.commit()

db.close()

print("✅ Base de datos poblada correctamente con países y números de emergencia")