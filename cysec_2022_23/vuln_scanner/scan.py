from duckduckgo_search import DDGS
import requests

def get_lista_url(keyword):
    lista_url = ["https://www.itsumbria.it"]
    ddgs = DDGS()
    risultati = [r for r in ddgs.text(keyword)]
    for r in risultati:
        lista_url.append("/".join(r["href"].split("/")[:3]))
    return lista_url

def check_form_7(url):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=user_agent)
    return "contact-form-7" in resp.text


if __name__ == "__main__":
    urls = get_lista_url("cesoie")
    for url in urls:
        try:
            check = check_form_7(url)
            if check:
                print("--------------> ", url)
            else:
                print(url)
        except:
            pass
