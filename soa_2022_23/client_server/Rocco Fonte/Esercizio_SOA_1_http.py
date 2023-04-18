# pip install requests
import requests
import json
user = input("Nome utente: ")
passw = input("Password: ")
url = f"http://127.0.0.1:8080/login?username={user}&password={passw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print("Login effettuata")
    else:
        print("Username o password errata")
else:
    print("Errore durante la richiesta HTTP")

url = "http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content != "":
        dizionario = json.loads(content)
        print(dizionario["nome"], dizionario["cognome"])
        print("Vive a",dizionario["citta"])
    else:
        print("BRUH")
else:
    print("Errore durante la richiesta HTTP anagrafica")