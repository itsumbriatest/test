import os
import platform
import re
import subprocess
from time import sleep
from threading import Event, Thread
import webbrowser

from bottle import default_app, post, request, route, run, template
import requests

from netsh import *
import compito


windows = platform.system() == "Windows"
print("Windows = ", windows)


if windows:
    # Woops! Much sneaky, very global
    ifaces = get_interfaces()
    #wlan = get_wlan()


@route("/")
def do_index():
    return template(f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>{compito.titolo} - {compito.data}</title>
        </head>
        <body>
            <div style="width: 500px; margin: auto">
                <h2>{compito.titolo} - {compito.data}</h2>
                <form action="/compito" method="POST">
                    <label for="name">Nome:</label><br>
                    <input type="text" id="first_name" name="first_name"></label><br><br>
                    <label for="email">Cognome:</label><br>
                    <input type="text" id="last_name" name="last_name" value=""><br><br>
                    <h1 style="color:red">Attendi le istruzioni del prof prima di iniziare</h1>
                    <input type="submit" value="INIZIA COMPITO">
                </form>
            </div>
        </body>
    </html>
    """)

def invia_mail(subject, body):
    url = compito.relay
    res = requests.post(url, data={
        "subject": subject,
        "body": body
    })


event = Event()
def inizio_compito(name):
    def controllo(event):
        while not event.is_set():
            try:
                subject = f"[ACHTUNG] {name} - {compito.titolo} {compito.data}"
                body = f"Lo studente  {name} si è connesso alla rete prima della fine del compito."
                invia_mail(subject, body)
                event.set()
            except:
                sleep(2)
    def inizio():
        subject = f"[INIZIO] {name} - {compito.titolo} {compito.data}"
        body = f"Lo studente {name} ha iniziato il compito."
        invia_mail(subject, body)
        sleep(3)
        if windows:
            for i in ifaces:
                if i.is_enabled():
                    i.disable()
            #disconnect_wlan()
        Thread(target=controllo, args=(event,)).start()
    Thread(target=inizio).start()


@post("/compito")
def do_compito():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    name = f"{last_name} {first_name}".upper()
    inizio_compito(name)
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>{compito.titolo} - {compito.data}</title>
        </head>
        <body>
            <div style="width: 500px; margin: auto">
                <h2>{compito.titolo} - {compito.data}</h2>
                <p>Il compito è composto da {len(compito.esercizi)} esercizi.</p>
                    <form action="/fine" method="POST">
                        <input type="hidden" name="first_name" value="{first_name}">
                        <input type="hidden" name="last_name" value="{last_name}">
"""
    for i, es in enumerate(compito.esercizi):
        html += f"""
<h3>Esercizio {i+1} ({es['punti']} punt{es['punti'] == 1 and "o" or "i"})</h3>
<p>{es['comando']}</p>
<p>
<textarea name="esercizio_{i+1}" cols="80" rows="25">{es['testo']}</textarea>
</p>
"""
    html += """
<h1 style="color:red">Attenzione, la consegna è definitiva</h1>
<input type="submit" value="CONSEGNA COMPITO">
</form></div></body></html>
"""
    return template(html)


@post("/fine")
def do_fine():
    event.set()
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    name = f"{last_name} {first_name}".upper()
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>{compito.titolo} - {compito.data}</title>
        </head>
        <body>
            <div style="width: 500px; margin: auto">
                <h1 style="color:red; display:block">Adesso non toccare più nulla, aspetta che il prof confermi di aver ricevuto il tuo compito</h1>
                <h2>{compito.titolo} - {compito.data}</h2>
                <p><b>Cognome:</b> {last_name}</p>
                <p><b>Nome:</b> {first_name}</p>
"""
    for i, es in enumerate(compito.esercizi):
        html += f"""
<h3>Esercizio {i+1} ({es['punti']} punt{es['punti'] == 1 and "o" or "i"})</h3>
<p>{es['comando']}</p>
<p>
<pre>{request.forms.get('esercizio_' + str(i+1))}</pre>
</p>
"""
    html += "</div></body></html>"
    def send():
        sleep(5)
        if windows:
            for i in ifaces:
                if i.is_enabled():
                    i.enable()
            #connect_wlan(wlan)
            sleep(60)
        subject = f"[CONSEGNA] {name} - {compito.titolo} {compito.data}"
        body = html.replace("display:block", "display:none")
        invia_mail(subject, body)
        os._exit(1)
    Thread(target=send).start()
    return template(html)


def main():
    def open_browser():
        sleep(3)
        webbrowser.open("http://localhost:8080")
    Thread(target=open_browser).start()
    run(host='localhost', port=8080, debug=True)


if __name__ == "__main__":        
    main()
