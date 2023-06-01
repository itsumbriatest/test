import requests

def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content.decode()
    else:
        print("GET REQUEST ERROR:", response.status_code)