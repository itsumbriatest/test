# pip install request
import requests
import json
username = input("Inserisci l'username: ")
password = input("Inserisci la password: ")

# 1) Login
url = f"http://127.0.0.1:8080/Login?username={username}&password={password}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print("Login succesful")
    else:
        print("Login failed")
else:
    print("Errore durante la richiesta HTTP")

# 2) Anagrafica
url = f"http://127.0.0.1:8080/Anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content != "":
        dizionario = json.loads("cognome")
        print(dizionario["nome"], dizionario["cognome"])
        print("Nato il, ", dizionario["nascita"])
else:
    print("Unauthorized!!! ACHTUNG!!!")
