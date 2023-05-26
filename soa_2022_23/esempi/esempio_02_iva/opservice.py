import math
from paste import httpserver
from bottle import default_app, request, route

def op_binaria(endpoint, f):
    def f_binaria():
        params = request.query.decode()
        x = float(params["x"])
        y = float(params["y"])
        return str(f(x, y))
    route(endpoint, "GET", f_binaria)

def op_unaria(endpoint, f):
    def f_unaria():
        params = request.query.decode()
        x = float(params["x"])
        return str(f(x))
    route(endpoint, "GET", f_unaria)

op_binaria("/somma", lambda x, y: x + y)
op_binaria("/sottrazione", lambda x, y: x - y)
op_binaria("/moltiplicazione", lambda x, y: x * y)
op_binaria("/divisione", lambda x, y: x / y)
op_binaria("/potenza", lambda x, y: x ** y)
op_unaria("/log10", lambda x: math.log10(x))
op_unaria("/sqrt", lambda x: math.sqrt(x))

httpserver.serve(default_app(), host="127.0.0.1", port=8080)