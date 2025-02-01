import cherrypy
import os

class DeSoPedia:
    @cherrypy.expose
    def index(self):
        return open(os.path.join('views', 'index.html'))

    

if __name__ == '__main__':
    cherrypy.quickstart(DeSoPedia(), '/', {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.abspath("static"),
        }
    })