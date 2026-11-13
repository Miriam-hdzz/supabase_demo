import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:
    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContacto(id_contacto)
        return render.actualizar_contacto(contacto)

    def POST(self, id_contacto):
        formulario = web.input()
        id_c = formulario['id_contacto']
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']

        model_contactos = ModelContactos()
        model_contactos.actualizarContacto(id_c, nombre, email, telefono)

        raise web.seeother('/contactos')