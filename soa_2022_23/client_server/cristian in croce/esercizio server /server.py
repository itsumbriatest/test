from paste import httpserver
from bottle import default_app, request, route

@route("/login")
def login():
    params = request.query.decode()
    u = params ["username"]
    p = params ["password"]
    print(f"Nuova login: '{u}' '{p}'")
    if  u == "cristian" and p == "123":
        return "ok"
    else:
        return "ko"



httpserver.serve(default_app(), host="127.0.0.1", port=8080)
