from livereload import Server
import os
path = os.path.abspath(os.path.dirname(__file__))

server = Server()
server.watch(f'{path}/*.py', "python app.py")
server.serve()