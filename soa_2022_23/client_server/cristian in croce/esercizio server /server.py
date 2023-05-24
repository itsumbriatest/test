from paste import httpserver
from bottle import default_app, request, route

login_ok = False

@route("/login")
def login():
    global login_ok 
    params = request.query.decode()
    u = params ["username"]
    p = params ["password"]
    print(f"Nuova login: '{u}' '{p}'")
    if  u == "cristian" and p == "123":
        login_ok = True
        return "ok"
    else:
        return "ko"

@route ("/anagrafica")
def anagrafica ():
    global login_ok
    anag = {
        "nome": "cristian", 
        "cognome": "in croce",
        "nascita": "1987-04-18"
    }
    if login_ok:
        return anag
    else:
        return False
    
httpserver.serve(default_app(), host="127.0.0.1", port=8080)
