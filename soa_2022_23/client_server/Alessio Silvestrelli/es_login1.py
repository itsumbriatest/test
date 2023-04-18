from paste import httpserver
from bottle import default_app, route, request

login_ok=False

@route("/login")
def index():
    global login_ok
    params=request.query.decode()
    if params["nome_utente"]=="ajeje" and params["password"]=="brazorf":
        login_ok=True
        return "OK"
    else:
        login_ok=False
        return "KO"

@route("/anagrafica")
def anagrafica():
    global login_ok  
    anag= {
        "nome": "Alessio", 
        "cognome": "Silvestrelli",
        "data nascita": "27/03/2001"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)