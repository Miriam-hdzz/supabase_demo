import web

from mvc.controllers.index import index
from mvc.controllers.contactos import Contactos

urls = (
    '/', 'index',
    '/contactos', 'Contactos',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
