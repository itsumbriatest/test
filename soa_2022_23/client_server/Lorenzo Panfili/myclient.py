import requests
user = input("Nome utente: ")
passw = input("Password: ")

url = f"http://127.0.0.1:8080/login?username={user}&password={passw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    if content == "OK":
        print ("Login successfull")
    else:
        print ("Wrong username or password")
else:
    print("Errore durante la richiesta HTTP")

url = "http://127.0.0.1:8080/anagrafica"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else: 
    print ("Errore durante la richiesta HTTP anagrafica")