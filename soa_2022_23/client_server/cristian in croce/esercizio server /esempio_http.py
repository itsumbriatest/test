# pip install request
import requests
nome = input("nome:")
psw = input("password:")
url = f"http://127.0.0.1:8080/login?username={nome}&password={psw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "ok":
        print ("login effetuato")
    else :
        print ("user o password errate")
    print(content)
else:
    print("Errore durante la richiesta HTTP")
