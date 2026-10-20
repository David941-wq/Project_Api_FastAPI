import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


#ya asignaste las formas de en que se va a encriptar el token y el tiempo de expiracion del token,
# debemos de usar esyto para los usuarios continua la guia de claude
