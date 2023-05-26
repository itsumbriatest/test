import requests


def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content.cdeode()
    else:
        print("GET TEQUEST ERROR:", response.status_code)
