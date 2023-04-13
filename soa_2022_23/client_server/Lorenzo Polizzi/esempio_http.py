# pip install request
import requests
url = "http://127.0.0.1:8080/test3"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print("Errore durante la richiesta HTTP")