import utils
import requests

print("Cosa vuoi fare?")
print("1- Inserisci Squadra")
print("2- Inserisci Giocatore")
print("3- Stampa lista squadre")
print("4- Stampa lista giocatori")

def inserisci_squadra(nome, budget):
    res =  utils.get(f"http://127.0.0.1:8080/inserisci_squadra?nome={nome}&budget={budget}")
    print("Inserimento squadra: ", res)

def inserisci_giocatore(squadra, nome, ruolo, costo):
    url =  f"http://127.0.0.1:8080/inserisci_squadra?squadra={squadra}&nome={nome}&budget={ruolo}&budget={costo}"
    res = utils.get(url)
    print("Inserimento giocatore: ", res)