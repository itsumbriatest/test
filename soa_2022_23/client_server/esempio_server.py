import os

from paste import httpserver  # multithread HTTP server
from bottle import default_app, post, request, route, run, template


@route("/")
def index():
    return "Hello, World!"


httpserver.serve(default_app(), host="127.0.0.1", port=8080)