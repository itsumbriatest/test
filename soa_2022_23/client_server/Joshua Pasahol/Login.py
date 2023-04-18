#questi import serve per il server
from paste import httpserver
from bottle import default_app, route, request

login_ok = False

@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if (params["username"] == "Chibitsune" and params["password"] == "pippo1234"):
        login_ok = True
        return "OK"
    else:
        login_ok = False
        return "KO"
    
@route("/anagrafica")
def anagrafica():
    global login_ok
    anag = {
        "Nome": "Joshua", 
        "Cognome": "Pasahol",
        "Nascita": "24/11/1999"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)