from Core.database import SessionLocal, engine, Base
from Models.Models import Localidad, NumeroEmergencia


def populate_database():
    """Pobla la BD con datos por defecto (solo si está vacía)."""
    db = SessionLocal()
    try:
        if db.query(Localidad).count() == 0:
            print("🌱 Poblando BD con datos...")

            paises = [
                {"nombre": "Colombia", "numeros": [("Policía", "112"), ("Bomberos", "119"), ("Ambulancia", "123")]},
                {"nombre": "Argentina", "numeros": [("Emergencias", "911"), ("Bomberos", "107")]},
                {"nombre": "México", "numeros": [("Emergencias", "911"), ("Cruz Roja", "065")]},
                {"nombre": "España", "numeros": [("Emergencias", "112"), ("Policía Nacional", "091"), ("Bomberos", "062")]},
                {"nombre": "Chile", "numeros": [("Carabineros", "131"), ("Bomberos", "133"), ("Ambulancia", "138")]},
                {"nombre": "Perú", "numeros": [("Policía", "105"), ("Bomberos", "106")]},
                {"nombre": "Brasil", "numeros": [("Bomberos", "190"), ("Policía", "192"), ("Ambulancia", "193")]},
                {"nombre": "Estados Unidos", "numeros": [("Emergencias", "911")]},
                {"nombre": "Canadá", "numeros": [("Emergencias", "911")]},
                {"nombre": "Francia", "numeros": [("Emergencias", "112"), ("Ambulancia", "015"), ("Policía", "017")]},
                {"nombre": "Alemania", "numeros": [("Policía", "110"), ("Emergencias", "112")]},
                {"nombre": "Reino Unido", "numeros": [("Emergencias", "999"), ("Emergencias UE", "112")]},
                {"nombre": "Italia", "numeros": [("Emergencias", "112"), ("Policía", "113")]},
                {"nombre": "Australia", "numeros": [("Emergencias", "000")]},
                {"nombre": "Japón", "numeros": [("Policía", "110"), ("Bomberos/Ambulancia", "119")]},
            ]

            for pais in paises:
                localidad = Localidad(nombre=pais["nombre"])
                db.add(localidad)
                db.commit()
                db.refresh(localidad)

                for nombre_servicio, numero in pais["numeros"]:
                    num_emergencia = NumeroEmergencia(
                        nombre=nombre_servicio,
                        numero=numero,
                        localidad_id=localidad.id
                    )
                    db.add(num_emergencia)

                db.commit()

            print("✅ BD poblada correctamente")
    finally:
        db.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    populate_database()
