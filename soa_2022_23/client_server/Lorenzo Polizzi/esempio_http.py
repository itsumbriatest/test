# pip install request
import requests
nome = input("Inserisci il nome utente: ")
psw = input("Inserisci la password: ")
url = f"http://127.0.0.1:8080/login?nome={nome}&psw={psw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print("Login effettuata")

    else:
        print("Username o password sbagliate")
else:
    print("Errore durante la richiesta HTTP")

url =  "http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print("Errore durante la richiesta HTTP anagrafica")