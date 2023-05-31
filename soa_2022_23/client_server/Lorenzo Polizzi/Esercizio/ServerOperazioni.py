from paste import httpserver
from bottle import default_app, request, route
import math

@route("/somma")
def somma():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    return str(x + y)

@route("/sottrazione")
def sottrazione():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    return str(x - y)

@route("/divisione")
def divisione():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    if y == 0:
        return str("Errore, il secondo numero è diverso da 0")
    else:
        return str(x/y)
    
@route("/moltiplicazione")
def prodotto():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    return str(x * y)

@route("/elevamento_a_potenza")
def potenza():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    return str(pow(x, y))

@route("/logaritmo")
def logaritmo():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    if x <= 0:
        return str("Errore, il primo numero deve essere maggiore di 0")
    else:
        return str(math.log10(x))
    
@route("/radice")
def radice():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    if x < 0:
        return str("Errore, il primo numero deve essere maggiore o uguale a 0")
    else:
        return str(math.sqrt(x))


httpserver.serve(default_app(), host="127.0.0.1", port=8080)