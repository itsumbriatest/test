from paste import httpserver
from bottle import default_app, request, route

login_ok = False
@route("/login")
def login():
    global login_ok
    params = request.query.decode()
    if params["username"] == "Alex10543!?" and params["password"] == "123456789":
        login_ok = True
        return "OK"
    else:
        login_ok = False
        return "KO"
    
@route("/anagrafica")
def anagrafica():
    global login_ok
    anag = {
        "nome":"Alessandro",
        "cognome":"Crispolti",
        "nascita":"2002-07-29"
    }
    if login_ok:
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)