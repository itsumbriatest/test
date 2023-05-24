from paste import httpserver
from bottle import default_app, request, route

@route("/somma")
def somma():
    params = request.query.decode()
    a=float(params["a"])
    b=float(params["b"])
    return str(a+b)

@route("/sottrazione")
def sottrazione():
    params = request.query.decode()
    a=float(params["a"])
    b=float(params["b"])
    if(a<b):
        return str(b-a)
    else:
        return str(a-b)

@route("/div")
def div():
    params = request.query.decode()
    a=float(params["a"])
    b=float(params["b"])
    return str(a/b)

@route("/pot")
def pot():
    params = request.query.decode()
    a=float(params["a"])
    b=float(params["b"])
    return str(pow(a,b))

@route("/radice")
def radice():
    params = request.query.decode()
    a=params["a"]
    sqrt(a)

@route("/log")
def log(a):
    params = request.query.decode()
    a=float(params["a"])
    return str(math.log10(a))


httpserver.serve(default_app(), host="127.0.0.1", port=8080)
