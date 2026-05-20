from sqlalchemy.orm import Session
from Models.Models import Usuario

class LoginRepository:
    def login(self, db: Session, nombre: str, contraseña: str):
        return db.query(Usuario).filter(Usuario.nombre == nombre, Usuario.contraseña == contraseña).first()