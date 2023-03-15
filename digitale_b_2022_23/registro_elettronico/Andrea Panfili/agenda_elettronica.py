from datetime import *


def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1



class Agenda_elettronica:
    def __init__(self, appuntamenti) -> None:
        self.appuntamenti = appuntamenti

    
    def menu(self):
        scelta = ""
        while scelta != "6":
            print("1) Inserire nuovo appuntamento")
            print("2) Modifica appuntamento")
            print("3) Aggiungi invitato")
            print("4) Rimuovi invitato")
            print("5) Cancella appuntamento")
            print("6) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.nuovo_appuntamento()
            elif scelta == "2":
                self.modifica_appuntamento()
            elif scelta == "3":
                self.aggiungi_invitato()
            elif scelta == "4":
                self.rimuovi_invitato()
            

    
    def nuovo_appuntamento(self):
        descrizione = input("Inserisci la descrizione: ")
        data = input("Inserisci la data: ")
        ricorrenza = input("Inserisci la ricorrenza: ")
        invitati = []
        appuntamento = Appuntamento(descrizione, data, ricorrenza, invitati)
        agenda.appuntamenti.append(appuntamento)
        
    
    def modifica_appuntamento(self):
        mostra_lista(self.appuntamenti)
        a = int(input("Quale appuntamento vuoi modificare? "))

        nuova_descrizione = input("Inserisci la nuova descrizione: ")
        self.appuntamenti[a].descrizione = nuova_descrizione

        nuova_data = input("Inserisci nuova data e ora (aaaa-mm-gg oo:mm): ")
        nuova_data = datetime.strptime(nuova_data, "%Y-%m-%d %H:%M")
        self.appuntamenti[a].data = nuova_data

        nuova_ricorrenza = input("Inserisci nuova ricorrenza: ")
        self.appuntamenti[a].ricorrenza = nuova_ricorrenza

    
    def aggiungi_invitato(self):
        mostra_lista(self.appuntamenti)
        a = int(input("A quale appuntamento vuoi aggiungere l'invitato? "))
        appuntamento = self.appuntamenti[a]

        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        email = input("Inserisci email: ")
        invitato = Invitato(nome, cognome, email)
        appuntamento.invitati.append(invitato)
        
    
    def rimuovi_invitato(self):
        mostra_lista(self.appuntamenti)
        a = int(input("A quale appuntamento vuoi rimuovere l'invitato? "))
        appuntamento = self.appuntamenti[a]
        mostra_lista(self.invitati)
        b = int(input("Quale invitato vuoi rimuovere? "))
        

    
    def cancella_appuntamento(self):
        pass



class Appuntamento:
    def __init__(self, descrizione, data, ricorrenza, invitati) -> None:
        self.descrizione = descrizione
        self.data = data 
        self.ricorrenza = ricorrenza
        self.invitati = invitati

    def __str__(self) -> str:
        return f"{self.descrizione}, {self.data}, {self.ricorrenza}, {self.invitati}"  #format string



class Invitato:
    def __init__(self, nome, cognome, email) -> None:
        self.nome = nome
        self.cognome = cognome
        self.email = email

    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.email}"
  
    def __repr__(self):
        return f"{self.nome}, {self.cognome}, {self.email}"

    


#MAIN

d1 = "2023-05-12 17:00:00"
d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
d2 = "2023-03-20 10:30:00"
d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")


i1 = Invitato("Andrea", "Panfili", "ap@gmail.com")
i2 = Invitato("Lorenzo", "Panfili", "lp@gmail.com")
i3 = Invitato("Massimiliano", "Muzi", "mm@gmail.com")
i4 = Invitato("Damiano", "Lupi", "dl@gmail.com")
a1 = Appuntamento("Calcetto", d1, "Settimanale", [i1, i2])
a2 = Appuntamento("Dentista", d2, "Annuale", [i3, i4])

agenda = Agenda_elettronica([a1, a2])
agenda.menu()


