from paste import httpserver
from bottle import default_app, request, route

@route("/login")
def login_ok():
    global login_ok
    params = request.query.decode()
    if params["username"]== "manuel" and params["password"] == "1234":
        return "OK"
    else:
        return "KO"
    
@route("/anagrafica")
def anagrafica():
    anag = {
        "nome" : "manuel",
        "cognome" : "pagliarulo",        
        "nascita" : "12/07/2003"}
    if login_ok :
        return anag
    else:
        return False

httpserver.serve(default_app(), host="127.0.0.1", port=8080)