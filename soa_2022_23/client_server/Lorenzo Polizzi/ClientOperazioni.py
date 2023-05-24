import requests
x = input("Inserisci il primo numero: ")
y = input("Inserisci il secondo numero: ")

print("\nSomma dei due numeri: ")
url = f"http://127.0.0.1:8080/somma?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

print("\nSottrazione dei due numeri: ")
url = f"http://127.0.0.1:8080/sottrazione?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

print("\nDivisione dei due numeri: ")
url = f"http://127.0.0.1:8080/divisione?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

print("\nProdotto dei due numeri: ")
url = f"http://127.0.0.1:8080/moltiplicazione?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

print("\nElevamento a potenza del primo numero e il secondo: ")
url = f"http://127.0.0.1:8080/elevamento_a_potenza?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

print("\nLogaritmo in base 10 del primo numero: ")
url = f"http://127.0.0.1:8080/logaritmo?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)

print("\nRadice del primo numero: ")
url = f"http://127.0.0.1:8080/radice?x={x}&y={y}"
response = requests.get(url)
if response.status_code == 200:
    content = response.content.decode()
    print(content)
else:
    print(response.status_code)