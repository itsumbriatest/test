# pip install request
import requests, json
a=input("inserisci nome utente: ")
b=input("inserisci password: ")
url = f"http://127.0.0.1:8080/login?nome_utente={a}&password={b}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content== "OK":
        print("credenziali corrette")
    else:
        print("credenziali errate")
else:
    print("Errore durante la richiesta HTTP")

url = "http://127.0.0.1:8080/anagrafica"
response=requests.get(url)
if response.status_code== 200:
    content=response.content.decode()
    if content!= "":
        dizionario=json.loads(content)
        print(dizionario["nome"], dizionario["cognome"])
        print("nato il ", dizionario["data nascita"])
    else:
        print("non autorizzato")
else:
    print("Errore durante la richiesta HTTP anagrafica")