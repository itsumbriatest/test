import requests
import json
# 1.Login
user = input("Nome utente: ")
passw = input("Password: ")
url = f"http://127.0.0.1:8080/login?username={user}&password={passw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print("Login effettuata")
    else:
        print("Wrong user name or password")
else:
    print("Errore durante la richiesta HTTP")

# 2.Anagrafica
url = "http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content !="":
        dizionario = json.loads(content)
        print(dizionario["nome"], dizionario["cognome"])
        print("Nato il", dizionario["nascita"])
    else:
        print("Unauthorized!! ACHTUNG!!!!")
    print(content)
else: 
    print("Errore durante la richiesta HTTP anagrafica")