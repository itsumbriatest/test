import requests

x = input("Inserisci il numero per calcolare l'iva: ")
y = 0.22

print("\nRisultato: ")
url = f"http://127.0.0.1:8081/iva?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)