from paste import httpserver
from bottle import default_app, route

@route("/")
def index():
    return "Hello, world!"

@route("/test2")
def secondo_test():
    return "Another test"

@route("/test3")
def secondo_test():
    my_dizionario = {
        "nome": "Antonio", 
        "cognome": "Asciolla"
    }
    return my_dizionario

httpserver.serve(default_app(), host="127.0.0.1", port=8080)
