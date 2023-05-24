import requests


class CalcolatriceClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def somma(self, num1, num2):
        data = {'num1': num1, 'num2': num2}
        response = requests.post(f"{self.server_url}/somma", json=data)
        result = response.json()
        return result['risultato']

    def sottrazione(self, num1, num2):
        data = {'num1': num1, 'num2': num2}
        response = requests.post(f"{self.server_url}/sottrazione", json=data)
        result = response.json()
        return result['risultato']

    def divisione(self, num1, num2):
        data = {'num1': num1, 'num2': num2}
        response = requests.post(f"{self.server_url}/divisione", json=data)
        result = response.json()
        return result['risultato']

    def potenza(self, base, esponente):
        data = {'base': base, 'esponente': esponente}
        response = requests.post(f"{self.server_url}/potenza", json=data)
        result = response.json()
        return result['risultato']

    def logaritmo(self, numero):
        data = {'numero': numero}
        response = requests.post(f"{self.server_url}/logaritmo", json=data)
        result = response.json()
        return result['risultato']

    def radice_quadrata(self, numero):
        data = {'numero': numero}
        response = requests.post(
            f"{self.server_url}/radice_quadrata", json=data)
        result = response.json()
        return result['risultato']


if __name__ == '__main__':
    server_url = 'http://localhost:8000'
    client = CalcolatriceClient(server_url)

    print(client.somma(5, 3))
    print(client.sottrazione(8, 2))
    print(client.divisione(10, 2))
    print(client.potenza(2, 3))
    print(client.logaritmo(100))
    print(client.radice_quadrata(16))
