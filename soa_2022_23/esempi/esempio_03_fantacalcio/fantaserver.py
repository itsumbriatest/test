from paste import httpserver
from bottle import default_app, request, route

class Giocatore:
    def __init__(self, nome, ruolo, prezzo):
        self.nome = nome
        self.ruolo = ruolo
        self.prezzo = prezzo
    
    def __str__(self):
        return f"{self.nome} ({self.ruolo}, {self.prezzo})"

class Squadra:
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget
        self.budget_rimasto = budget
        self.giocatori = []
        self.giocatori_rimasti_per_ruolo = {
            "Attaccante": 6,
            "Centrocampista": 8,
            "Difensore": 8,
            "Portiere": 3
        }
    
    def inserisci_giocatore(self, g):
        if g.prezzo < 0:
            return "ERRORE: prezzo non valido"
        if g.ruolo != "Portiere" and g.ruolo != "Difensore" and g.ruolo != "Centrocampista" and g.ruolo != "Attaccante":
            return "ERRORE: ruolo non valido"
        if self.giocatori_rimasti_per_ruolo[g.ruolo] == 0:
            return "ERRORE: ruolo pieno"
        if self.budget_rimasto < g.prezzo:
            return "ERRORE: non hai abbastanza fantacrediti"
        self.giocatori.append(g)
        self.giocatori_rimasti_per_ruolo[g.ruolo] -= 1
        self.budget_rimasto -= g.prezzo
        return "OK"
    
    def __str__(self):
        return f"{self.nome} ({self.budget})"

lista_squadre = []

@route("/inserisci_squadra")
def inserisci_squadra():
    global lista_squadre
    params = request.query.decode()
    nome = params["nome"]
    budget = int(params["budget"])
    s = Squadra(nome, budget)
    for squadra in lista_squadre:
        if squadra.nome == s.nome:
            return "ERRORE: Squadra duplicata"
    lista_squadre.append(s)
    return "OK"

@route("/inserisci_giocatore")
def inserisci_giocatore():
    global lista_squadre
    params = request.query.decode()
    nome_squadra = params["nome_squadra"]
    nome = params["nome"]
    ruolo = params["ruolo"]
    prezzo = int(params["prezzo"])
    for squadra in lista_squadre:
        if squadra.nome == nome_squadra:
            g = Giocatore(nome, ruolo, prezzo)
            return squadra.inserisci_giocatore(g)
    return "ERRORE: squadra non trovata"

@route("/lista_squadre")
def lista_squadre():
    global lista_squadre
    return ", ".join([str(s) for s in lista_squadre])

@route("/lista_giocatori")
def lista_giocatori():
    global lista_squadre
    params = request.query.decode()
    nome_squadra = params["nome_squadra"]
    for squadra in lista_squadre:
        if squadra.nome == nome_squadra:
            return ", ".join([str(g) for g in squadra.giocatori])
    return "ERRORE: squadra non trovata"

httpserver.serve(default_app(), host="127.0.0.1", port=8080)