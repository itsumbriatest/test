import requests
import json

# URL del server Bottle
base_url = 'http://localhost:8080'

def crea_squadra(nome, budget):
    url = f'{base_url}/crea_squadra'
    data = {
        'nome': nome,
        'budget': budget
    }
    response = requests.post(url, json=data)
    return response.text

def inserisci_giocatore(nome_squadra, nome_giocatore, ruolo_giocatore, costo_giocatore):
    url = f'{base_url}/inserisci_giocatore'
    data = {
        'nome_squadra': nome_squadra,
        'nome_giocatore': nome_giocatore,
        'ruolo': ruolo_giocatore,
        'costo': costo_giocatore
    }
    response = requests.post(url, json=data)
    return response.text

def lista_squadre():
    url = f'{base_url}/lista_squadre'
    response = requests.get(url)
    data = response.json()
    return data['squadre']

def leggi_giocatori_squadra(nome_squadra):
    url = f'{base_url}/leggi_giocatori_squadra'
    data = {
        'nome_squadra': nome_squadra
    }
    response = requests.post(url, json=data)
    data = response.json()
    return data['rosa_squadra']

# Esempi di utilizzo del client
print(crea_squadra('Squadra1', 300))
print(crea_squadra('Squadra2', 400))

print(inserisci_giocatore('Squadra1', 'Giocatore1', 'portiere', 50))
print(inserisci_giocatore('Squadra1', 'Giocatore2', 'difensore', 30))
print(inserisci_giocatore('Squadra1', 'Giocatore3', 'centrocampista', 40))

print(lista_squadre())

print(leggi_giocatori_squadra('Squadra1'))
