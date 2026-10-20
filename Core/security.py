from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

Secret_key = os.getenv("SECRET_KEY")
Algorithm = os.getenv("ALGORITHM")
Access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def VerifyPassword(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    data debe incluir al menos: {"sub": str(usuario.id), "rol": "usuario" | "psicologo"}
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=Access_token_expire_minutes))
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, Secret_key, algorithm=Algorithm)

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, Secret_key, algorithms=[Algorithm]) 
        return payload #mejora el manejo de los atributos para el cliente
    except JWTError as e:
        print("error", e)
        print("Tipo de error:", type(e))
        raise ValueError("Token inválido o expirado")