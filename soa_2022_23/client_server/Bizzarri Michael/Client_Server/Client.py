import requests
import json

class Operazioni:

    def __init__(self):
        pass

    def somma(self,a,b):
        url = f"http://127.0.0.1:8080/somma?a={a}&b={b}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode()
            return float(content)
        else:
            print("errore")

    def div(self,a,b):
        url = f"http://127.0.0.1:8080/somma?a={a}&b={b}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode()
            return float(content)
        else:
            print("errore")

    def pot(self,a,b):
        url = f"http://127.0.0.1:8080/somma?a={a}&b={b}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode()
            return float(content)
        else:
            print("errore")

    def radice(self,a):
        url = f"http://127.0.0.1:8080/somma?a={a}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode()
            return float(content)
        else:
            print("errore")

    def log(self,a):
        url = f"http://127.0.0.1:8080/somma?a={a}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode()
            return float(content)
        else:
            print("errore")

    def sottrazione(self,a,b):
        url = f"http://127.0.0.1:8080/somma?a={a}&b={b}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode()
            return float(content)
        else:
            print("errore")

#MAIN
op=Operazioni()
a=float(input("Inserisci un valore: "))
b=float(input("Inserisci un valore: "))

somma=op.somma(a,b)
sottrazione=op.sottrazione(a,b)
div=op.div(a,b)
radice=op.radice(a)
pot=op.pot(a,b)
log=op.log(a)
print("La somma è: ",somma)
print("La sottrazione è: ",sottrazione)
print("La divisione è: ",div)
print("La radice è: ",radice)
print("La potenza è: ",pot)
print("Il logaritmo è: ",log)