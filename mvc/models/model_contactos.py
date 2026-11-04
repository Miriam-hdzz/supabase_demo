import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self .supabase: Client = create_client(
                os.environ.get("SUPABASE_URL",""),
                os.environ.get("SUPABASE_KEY","")
            )
        except Exception as error:
            print(f"Error 100: {error.args[0]}"))

    def obtenerContactos(self):
        #SELECT * FROM contactos;
        response = self.supabase
        return response.data

    def insertarContacto(self, nombre, email, telefono):
        response = self.supabase.table("contactos").insert({"nombre": nombre, "email": email, "telefono": telefono}).execute()
        return response.data

    def borrarContacto(self, id_contactos):
        response = self.supabase.table("contactos").delete().eq("id_contactos", id_contactos).execute()
        return response.data

    def actualizarContacto(self, id_contactos, nombre, email, telefono):
        response = self.supabase.table("contactos").update({"nombre": nombre, "email": email, "telefono": telefono}).eq("id_contactos", id_contactos).execute()
        return response.data


if __name__ == "__main__": 
    model_contactos = ModelContactos()# sirve para crear una instancia de la clase ModelContactos
    print(model_contactos.obtenerContactos()) # imprime la lista de contactos obtenidos desde Supabase
    print(model_contactos.buscarContacto(14)) # imprime el contacto con id 14 obtenido desde Supabase
    print(model_contactos.insertarContacto("Juan Perez", "juan.perez@example.com", "1234567890")) # inserta un nuevo contacto
    print(model_contactos.borrarContacto(14)) # borra el contacto con id 14 
    print(model_contactos.actualizarContacto(14, "Juan García", "juan.garcia@example.com", "0987654321")) # actualiza el contacto con id 14
   
   
    #REQUERIMIENTOS:
#1 obtener contacto ()
#2 buscar contacto (id)
#3 insertar contacto (nombre, email, telefono)
#4 borrar contacto (id_contactos)
#5 actualizar contacto (id_contactos, nombre, email, telefono)