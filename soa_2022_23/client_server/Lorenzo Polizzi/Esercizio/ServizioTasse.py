from paste import httpserver
from bottle import default_app, request, route
import requests
import math

#Risultato
@route("/iva")
def calcola_iva():
    params = request.query.decode()
    user = float(params["u"])
    passw = float(params["p"])
    url = f"http://127.0.0.1:8082/login?nome={user}&psw={passw}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode()
        if (content == "OK"):
            x = float(params["x"])
            url = f"http://127.0.0.1:8080/moltiplicazione?x={x}&y=0.22"
            try:
                response = requests.get(url)
                return response
            except:
                return "Errore: il servizio operazioni non è disponibile?"
        else:
            return "Utente e password errate"
    else:
        print(response.status_code)
        

httpserver.serve(default_app(), host="127.0.0.1", port=8081)


