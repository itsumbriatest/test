from paste import httpserver
from Bottle import default_app, request, route

login_ok = False

@route("/login")
def index():
    global login_ok
    params = request.query.decode()
    if params["username"] == "Leonardo" and params["password"] == "Pippo":
        login_ok = True
        return "OK"
    else:
        return "KO"
    
@route("/anagrafica")
def anagrafica():
    global login_ok 
    anag = {
        "nome": "Leonardo",
        "cognome": "Bandini",
        "nascita": "14-08-2000"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)



