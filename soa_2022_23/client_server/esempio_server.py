import os

from paste import httpserver
from bottle import default_app, route

@route("/")
def index():
    return "Hello, World!"

httpserver.serve(default_app(), host="127.0.0.1", port=8080)