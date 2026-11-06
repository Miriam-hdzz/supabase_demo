import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL",""),
                os.environ.get("SUPABASE_KEY","")
            )
        except Exception as error:
            print(f"Error 100: {error.args[0]}")

    def obtenerContactos(self):
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
        return response.data

    def insertarContacto(self, nombre, email, telefono): 
        datos= {"nombre": nombre, "email": email, "telefono": telefono}
        response = self.supabase.table("contactos").insert(datos).execute()
        return response.data

    def borrarContacto(self, id_contacto):
        response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
        return response.data

    def actualizarContacto(self, id_contacto, nombre, email, telefono):
        response = self.supabase.table("contactos").update({"nombre": nombre, "email": email, "telefono": telefono}).eq("id_contacto", id_contacto).execute()
        return response.data


if __name__ == "__main__": 
    model_contactos = ModelContactos()
    
    print(model_contactos.obtenerContactos())# obtiene todos los contactos
    print(model_contactos.buscarContacto(1))# busca un contacto por id
    print(model_contactos.insertarContacto("Yos", "yoselin@example.com", "123444566666"))#inserta un contacto
    print(model_contactos.borrarContacto(3))#borra un contacto por id
    print(model_contactos.actualizarContacto(1, "Mimi", "mimi@example.com", "098-765-43211"))#actualiza un contacto por id

        #REQUERIMIENTOS:
#1 obtener contacto ()
#2 buscar contacto (id)
#3 insertar contacto (nombre, email, telefono)
#4 borrar contacto (id_contactos)
#5 actualizar contacto (id_contactos, nombre, email, telefono)