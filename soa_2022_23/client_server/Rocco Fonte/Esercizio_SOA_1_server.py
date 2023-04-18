from paste import httpserver
from bottle import default_app, route, request

@route("/login")
def index():
    global login_ok
    user = "Rocco"
    passw = "123"
    params = request.query.decode()
    if params["username"] == user and params["password"] == passw:
        login_ok = True
        return "OK"
    else:
        login_ok = False
        return "KO"

@route("/anagrafica")
def anagrafica():
    anag = {
        "nome": "Rocco",
        "cognome": "Fonte",
        "citta": "Trapani"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)
    
