import random
from datetime import *

def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Agenda:
    def __init__(self,appuntamenti):
        self.appuntamenti=appuntamenti

    def menu(self):
        scelta = ""
        while scelta != "6":
            print("1) Inserisci nuovo appuntamento")
            print("2) Modifica appuntamento esistente")
            print("3) Aggiungi invitato all'appuntamento")
            print("4) Rimuovi invitato dall'appuntamento")
            print("5) Cancella appuntamento")
            print("6) Exit")
            scelta = input("Scelta: ")
            if scelta == "1":
                descr=input("Inserisci descrizione: ")
                data_ora=datetime.strptime(input("Inserisci la data (Y-m-d H:M:S): "), "%Y-%m-%d %H:%M:%S")
                ric=input("Inserisci la ricorrenza: ")
                nuovo_app = Appuntamento(descr, data_ora, ric, [])
                self.appuntamenti.append(nuovo_app)
                print("--------------------------------------------")
                print("Lista appuntamenti")
                mostra_lista(self.appuntamenti)
                print("--------------------------------------------")
            elif scelta == "2":
                mostra_lista(self.appuntamenti)
                n=int(input("Quale appuntamento vuoi modificare? "))
                descr=input("Inserisci la nuova descrizione: ")
                data_ora=datetime.strptime(input("Inserisci la nuova data (Y-m-d H:M:S): "), "%Y-%m-%d %H:%M:%S")
                ric=input("Inserisci la nuova ricorrenza: ")
                self.modifica_app(n,descr,data_ora,ric)
                print("--------------------------------------------")
                print("Lista appuntamenti")
                mostra_lista(self.appuntamenti)
                print("--------------------------------------------")
            elif scelta == "3":
                mostra_lista(self.appuntamenti)
                n=int(input("Quale appuntamento vuoi modificare? "))
                nome=input("Inserisci il nome dell'invitato: ")
                cognome=input("Inserisci il cognome dell'invitato: ")
                email=input("Inserisci l'email dell'invitato: ")
                nuovo_inv=Invitato(nome,cognome,email)
                self.aggiungi_inv(n,nuovo_inv)
                print("--------------------------------------------")
                print("Lista invitati")
                mostra_lista(self.appuntamenti[n].invitati)
                print("--------------------------------------------")
            elif scelta == "4":
                mostra_lista(self.appuntamenti)
                n=int(input("Quale appuntamento vuoi modificare? "))
                mostra_lista(self.appuntamenti[n].invitati)
                n2=int(input("Quale invitato vuoi eliminare? "))
                self.rimuovi_inv(n,n2)
                print("--------------------------------------------")
                print("Lista invitati")
                mostra_lista(self.appuntamenti[n].invitati)
                print("--------------------------------------------")
            elif scelta == "5":
                mostra_lista(self.appuntamenti)
                n=int(input("Quale appuntamento vuoi modificare? "))
                self.cancella_app(n)
                print("--------------------------------------------")
                print("Lista appuntamenti")
                mostra_lista(self.appuntamenti)
                print("--------------------------------------------")

    def modifica_app(self,n,descrizione,data_ora,ricorrenza):
        self.appuntamenti[n].descrizione=descrizione
        self.appuntamenti[n].data_ora=data_ora
        self.appuntamenti[n].ricorrenza=ricorrenza

    def aggiungi_inv(self,n,nuovo_inv):
        self.appuntamenti[n].invitati.append(nuovo_inv)

    def rimuovi_inv(self,n,n2):
        del self.appuntamenti[n].invitati[n2]

    def cancella_app(self,n):
        del self.appuntamenti[n]

class Appuntamento:
    def __init__(self,descrizione,data_ora,ricorrenza,invitati):
        self.descrizione=descrizione
        self.data_ora=data_ora
        self.ricorrenza=ricorrenza
        self.invitati=invitati

    def __str__(self):
        return f"{self.descrizione},{self.data_ora},{self.ricorrenza}"

class Invitato:
    def __init__(self,nome,cognome,email):
        self.nome=nome
        self.cognome=cognome
        self.email=email

    def __str__(self):
        return f"{self.nome},{self.cognome},{self.email}"

#MAIN
i1=Invitato("Mario","Rossi","m.r@gmail.com")
i2=Invitato("Luigi","Verdi","l.v@gmail.com")
i3=Invitato("Michael","Bizzarri","m.b@gmail.com")
i4=Invitato("Leonardo","Bandini","l.b@gmail.com")
a1=Appuntamento("Dentista",datetime.strptime("2023-03-01 18:00:00", "%Y-%m-%d %H:%M:%S"),"nessuna",[i1])
a2=Appuntamento("Calcetto",datetime.strptime("2023-03-11 21:30:00", "%Y-%m-%d %H:%M:%S"),"settimanale",[i2,i4])
a3=Appuntamento("Scuola",datetime.strptime("2023-03-01 9:00:00", "%Y-%m-%d %H:%M:%S"),"giornaliera",[i1,i2,i3,i4])
a=Agenda([a1,a2,a3])
a.menu()