from paste import httpserver
from bottle import default_app, route, request

login_ok = False

@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if params ["username"] == "pippo" and params ["password"] == "topolino":
        login_ok = True
        return "OK"
    else:
        return "KO"
    
@route("/anagrafica")
def angrafica():
    global login_ok
    anag = {
        "nome" : "Lorenzo",
        "cognome" : "Panfili",
        "nascita" : "2003-04-09"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)