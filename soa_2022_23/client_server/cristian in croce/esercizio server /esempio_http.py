# pip install request
import requests
nome = input("nome:")
psw = input("password:")

# 1) Login
url = f"http://127.0.0.1:8080/login?username={nome}&password={psw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "ok":
        print ("login effetuato")
    else :
        print ("user o password errate")
else:
    print("Errore durante la richiesta HTTP")

# 2) Anag
url = f"http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print (content)
else:
    print("errore durante la richiesta http angarafica")

