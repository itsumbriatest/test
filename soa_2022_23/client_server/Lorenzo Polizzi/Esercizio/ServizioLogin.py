from paste import httpserver
from bottle import default_app, request, route
import requests
import math

@route("/login")
def login():
    params = request.query.decode()
    if params["nome"] == "Lorenzo1" and params["psw"] == "1234":
        return "OK"
    else:
        return "KO"


httpserver.serve(default_app(), host="127.0.0.1", port=8082)