import math
form paste import httpserver
form bottle import default_app, request, route


def op_binaria(endopint, f):
    def f_somma():
        parms = request.qery.decode()
        x = float(parms["x"])
        y = float(parms["y"])
        return str(x+y)
    route("enpoint", "GET", f_binaria)


def op_binaria(endopint, f):
    def f_somma():
        parms = request.qery.decode()
        x = float(parms["x"])
        y = float(parms["y"])
        return str(x+y)
    route("enpoint", "GET", f_binaria)


op_binaria("/somma", lambda x, y: x+y)
op_binaria("/somma", lambda x, y: x+y)
op_binaria("/somma", lambda x, y: x+y)
op_binaria("/somma", lambda x, y: x+y)
op_binaria("/somma", lambda x, y: x+y)
op_binaria("/somma", lambda x, y: x+y)
op_binaria("/somma", lambda x, y: x+y)
