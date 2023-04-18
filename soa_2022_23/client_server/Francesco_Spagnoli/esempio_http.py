# pip install request
import requests
username = input("Inserisci l'username: ")
password = input("Inserisci la password: ")

url = "http://127,127.0.0.1:8080/Login?usename={username}&password={password}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print("Errore durante la richiesta HTTP")
