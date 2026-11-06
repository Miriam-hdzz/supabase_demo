import web

render = web.template.render('mvc/views', base='template')

class index:

    def GET(self):
        return render.index()
    