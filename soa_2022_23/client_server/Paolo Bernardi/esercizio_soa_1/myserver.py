from paste import httpserver
from bottle import default_app, request, route

login_ok = False

@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if params["username"] == "pippo" and params["password"] == "topolino":
        login_ok = True
        return "OK"
    else:
        return "KO"

@route("/anagrafica")
def anagrafica():
    global login_ok
    anag = {
        "nome": "Piero",
        "cognome": "Brandola",
        "nascita": "1982-01-16"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)
