from paste import httpserver
from bottle import default_app, request, route

login_ok = False

@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if params["username"] == "Matteo" and params["password"] == "1974":
        login_ok = True
        return "OK"
    else:
        return "KO"
    
@route("/anagrafica")
def anagrafica():
    global login_ok
    anag = {
        "Nome: ": "Matteo",
        "Cognome: ": "Giacomini",
        "Data di nascita: ": "26/02/2003",
        "Città: ": "Terni",
        "CF: ": "GCMMTT03B26L117A"
    }
    if login_ok:
        return anag
    else:
        return False


httpserver.serve(default_app(), host="127.0.0.1", port=8080)