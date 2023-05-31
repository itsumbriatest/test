import requests

nome = input("Inserisci il nome utente: ")
psw = input("Inserisci la password: ")
x = input("Inserisci il numero per calcolare l'iva: ")

print("\nRisultato: ")
url = f"http://127.0.0.1:8081/iva?x={x}&u={nome}&p={psw}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

#---------------------
