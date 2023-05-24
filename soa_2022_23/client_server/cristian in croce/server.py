import math
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MathServiceHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        operation = self.path[1:]
        result = None

        if operation == 'somma':
            num1 = data['num1']
            num2 = data['num2']
            result = num1 + num2
        elif operation == 'sottrazione':
            num1 = data['num1']
            num2 = data['num2']
            result = num1 - num2
        elif operation == 'divisione':
            num1 = data['num1']
            num2 = data['num2']
            result = num1 / num2
        elif operation == 'potenza':
            base = data['base']
            esponente = data['esponente']
            result = base ** esponente
        elif operation == 'logaritmo':
            numero = data['numero']
            result = math.log10(numero)
        elif operation == 'radice_quadrata':
            numero = data['numero']
            result = math.sqrt(numero)

        if result is not None:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'risultato': result}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'errore': 'Operazione non supportata'}
            self.wfile.write(json.dumps(response).encode())


def run_server():
    host = 'localhost'
    port = 8000
    server_address = (host, port)
    httpd = HTTPServer(server_address, MathServiceHandler)
    print(f"Server in esecuzione su {host}:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
