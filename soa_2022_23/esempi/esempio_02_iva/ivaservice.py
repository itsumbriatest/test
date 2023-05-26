from paste import httpserver
from bottle import default_app, request, route
import opservice_client

@route("/iva")
def calcola_iva():
    params = request.query.decode()
    prezzo = float(params["prezzo"])
    opservice = opservice_client.OpService()
    return str(opservice.moltiplicazione(prezzo, 0.22))

httpserver.serve(default_app(), host="127.0.0.1", port=8081)
