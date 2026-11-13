import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:
    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContacto(id_contacto)
        return render.borrar_contacto(contacto)

    def POST(self, id_contacto):
        formulario = web.input()
        id_c = formulario['id_contacto']

        model_contactos = ModelContactos()
        model_contactos.eliminarContacto(id_c)

        raise web.seeother('/contactos')