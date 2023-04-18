#pip install request
import requests
nome_utente = input("Nome utente: ")
password = input("Password: ")
url = f"http://127.0.0.1:8080/login?username={nome_utente}&password={password}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print("Login effettuato")
    else:
        print("Attaccate al cazzo")
else:
    print("Errore durante la richiesta HTTP")

url = "http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else: 
    print("Errore durante la richiesta HTTP anagrafica")