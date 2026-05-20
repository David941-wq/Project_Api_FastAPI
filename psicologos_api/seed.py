from Core.database import SessionLocal, engine, Base
from Models.Models import Localidad, NumeroEmergencia

def populate_database():
    """Pobla la BD con datos por defecto"""
    db = SessionLocal()
    
    if db.query(Localidad).count() == 0:
        print("🌱 Poblando BD con datos...")
        
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
            {"nombre": "Australia", "numeros": [0]},
            {"nombre": "Japón", "numeros": [110, 119]},
        ]
        
        for pais in paises:
            localidad = Localidad(nombre=pais["nombre"])
            db.add(localidad)
            db.commit()
            
            for numero in pais["numeros"]:
                num_emergencia = NumeroEmergencia(numero=numero, localidad_id=localidad.id)
                db.add(num_emergencia)
            
            db.commit()
        
        print("✅ BD poblada correctamente")
    
    db.close()

# Para ejecutar manualmente desde línea de comandos
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    populate_database()