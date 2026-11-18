import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

#lee las variables de entorno del archivo .env
load_dotenv()

# Configura el sistema de logging
logger = logging.getLogger(__name__)

class AuthUsers:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")

    def iniciarSesion(self, email:str, pasword:str):
        try:
            response = self.supabase.auth.sign_in_with_password(
                {
                "email": email,
                "password": pasword
            }
            )
            print(f"Inicio de sesión exitoso: {response}")
        except Exception as error:
            logger.error(f"ERROR 101: {str(error)}")
            print(f"ERROR 101: {str(error)}")

    def registrarUsuario(self, email, pasword:str)->str | None:
        try:
            response = 


if __name__ == "__main__":
    print("Autenticacion de usuarios")
    objeto = AuthUsers()
    print(objeto.iniciarSesion("miris@gmail.com","123456"))
    print(objeto.iniciarSesion("miris@gmail.com", "123456"))
                         
        