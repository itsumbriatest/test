from paste import httpserver
from bottle import default_app, request, route

login_ok = False

@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if params["nome"] == "Lorenzo1" and params["psw"] == "1234":
        login_ok = True
        return "OK"
    else:
        return "KO"

@route("/anagrafica")
def anagrafica():
    global login_ok
    anag = {
        "nome": "Lorenzo", 
        "cognome": "Polizzi",
        "nascita": "10-06-2002"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)
