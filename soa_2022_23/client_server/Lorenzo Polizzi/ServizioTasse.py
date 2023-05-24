from paste import httpserver
from bottle import default_app, request, route
import requests
import math

#Risultato
@route("/iva")
def calcola_iva():
    params = request.query.decode()
    x = float(params["x"])
    y = float(params["y"])
    url = f"http://127.0.0.1:8080/moltiplicazione?x={x}&y={y}"
    try:
        response = requests.get(url)
        return response
    except:
        return "Errore: il servizio operazioni non è disponibile?"


httpserver.serve(default_app(), host="127.0.0.1", port=8081)


