import utils

def inserisci_squadra(nome, budget):
    res = utils.get(f"http://127.0.0.1:8080/inserisci_squadra?nome={nome}&budget={budget}")
    print("INSERIMENTO SQUADRA:", res)

def inserisci_giocatore(squadra, nome, ruolo, prezzo):
    url = f"http://127.0.0.1:8080/inserisci_giocatore?squadra={squadra}&nome={nome}&ruolo={ruolo}&prezzo={prezzo}"
    res = utils.get(url)
    print("INSERIMENTO GIOCATORE:", res)

# Main
print("FANTATEST")
inserisci_squadra("Juventus", 500)
inserisci_squadra("Terni Est", 10)

inserisci_giocatore("Juventus", "Michel Platini", "Attaccante", 150)
inserisci_giocatore("Terni Est", "Erling Haaland", "Attaccante", 350)
inserisci_giocatore("Terni Est", "Paolo Bernardi", "Difensore", -1)
