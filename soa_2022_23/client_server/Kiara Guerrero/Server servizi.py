from paste import httpserver
from bottle import default_app, request, route

login_ok = False

@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if params["username"] == "Kiara" and params["password"] == "raton":
        login_ok = True
        return "OK"
    else:
        login_ok = False
        return "KO"
    
@route("/anagrafica")
def anagrafica():
    global login_ok
    anag = {
        "nome": "Kiara",
        "cognome": "Guerrero",
        "nascita": "25/11/2001"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)

