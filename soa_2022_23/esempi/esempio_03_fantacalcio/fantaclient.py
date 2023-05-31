import utils

def inserisci_squadra(nome, budget):
    res = utils.get(f"http://127.0.0.1:8080/inserisci_squadra?nome={nome}&budget={budget}")
    print("INSERIMENTO SQUADRA:", res)

def inserisci_giocatore(squadra, nome, ruolo, prezzo):
    url = f"http://127.0.0.1:8080/inserisci_giocatore?nome_squadra={squadra}&nome={nome}&ruolo={ruolo}&prezzo={prezzo}"
    res = utils.get(url)
    print("INSERIMENTO GIOCATORE:", res)

def lista_squadre():
    url = f"http://127.0.0.1:8080/lista_squadre"
    res = utils.get(url)
    print("LISTA_SQUADRE:", res)

def lista_giocatori(squadra):
    url = f"http://127.0.0.1:8080/inserisci_giocatore?nome_squadra={squadra}"
    res = utils.get(url)
    print("LISTA GIOCATORI:", res)

# Main
print("FANTATEST")
inserisci_squadra("Juventus", 500)
inserisci_squadra("Terni Est", 10)

inserisci_giocatore("Juventus", "Michel Platini", "Attaccante", 150)
inserisci_giocatore("Terni Est", "Erling Haaland", "Attaccante", 350)
inserisci_giocatore("Terni Est", "Paolo Bernardi", "Difensore", -1)

lista_squadre()
lista_giocatori("Terni Est")