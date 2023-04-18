# pip install request
#l'import request serve per il client
import json
import requests

username = input("Inserisci l'username: ")
password = input("Inserisci il password: ")
url = f"http://127.0.0.1:8080/login?username={username}&password={password}" #le {} serve per utilita generiche
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print("Login successful. \t", "\nWelcome Player", username,".")
    else:
        print("Wrong username or password. ", "\nAccess Denied")
else:
    print("Errore durante la richiesta HTTP")

#2 anagrafica
url = "http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content != "":
        dizionario = json.loads(content)
        print(dizionario["Nome"], dizionario["Cognome"])
        print("Nato il", dizionario["Nascita"])
    else:
        print("Unauthorized!!!")
else:
    print("Errore durante la richiesta HTTP anagrafica")