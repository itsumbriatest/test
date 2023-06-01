from paste import httpserver
from bottle import default_app, request, route
import math

class Giocatore:
    def __init__(self, nome, ruolo, costo):
        self.nome = nome
        self.ruolo = ruolo
        self.costo = costo

    def __str__(self) -> str:
        return f"{self.nome} ({self.ruolo}, {self.costo})"

class Squadra:
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget
        self.giocatori = []

    def inserisci_giocatore(self, g):
        self.giocatori.append(g)

    def __str__(self) -> str:
        return f"{self.nome} ({self.budget})"
    

lista_squadre = []


@route("inserisci_giocatore")
def inserisciGiocatore():
    global lista_squadre
    params = request.query.decode()
    nome_squadra = params["nome_squadra"]
    nome = params["nome"]
    ruolo = params["ruolo"]
    costo = float(params["costo"])
    if costo < 0:
        return "Errore: prezzo non valido"
    for squadra in lista_squadre:
        if squadra.nome == nome_squadra:
            giocatore = Giocatore(nome, ruolo, costo)
            squadra.inserisci_giocatore(giocatore)
            return "OK"
    return "ERRORE: squadra non trovata"
        
@route("inserisci_squadra")
def inserisciSquadra():
    params = request.query.decode()
    nome = params["nome"]
    budget = float(params["budget"])
    squadra = Squadra(nome, budget)
    for squadraControl in lista_squadre:
        if squadraControl.nome == squadra.nome:
            return "Squadra duplicata"
    lista_squadre.insert(squadra)
    return "OK"


@route("stampa_lista_squadre")
def stampaSquadre():
    l = ""
    for squadra in lista_squadre:
        l += str(squadra) + "\n"
    return l
        

@route("leggi_giocatori_squadra")
def stampaGiocatore():
    pass
    

