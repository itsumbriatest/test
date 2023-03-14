from datetime import *

def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Appuntamento:
    def __init__(self, descrizione, data_ora, ricorrenza, invitati):
        self.descrizione = descrizione
        self.data_ora = data_ora
        self.ricorrenza = ricorrenza
        self.invitati = invitati

    def __str__(self):
        return self.descrizione + " " + self.data_ora.strftime("%Y-%m-%d %H:%M") + " " + self.ricorrenza 

class Invitato:
    def __init__(self, nome, cognome, mail):
        self.nome = nome
        self.cognome = cognome
        self.mail = mail

    def __str__(self):
        return self.nome + " " + self.cognome + " " + self.mail

class Agenda:
    def __init__(self, appuntamenti):
        self.appuntamenti = appuntamenti

    def menu(self):
        scelta = ""
        while scelta != "6":
            print("1) Inserire un nuovo appuntamento")
            print("2) Modificare la descrizione, la data, l’ora e la ricorrenza di un appuntamento esistente")
            print("3) Aggiungere un invitato ad un appuntamento")
            print("4) Rimuovere un invitato da un appuntamento")
            print("5) Cancellare un appuntamento")
            print("6) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.inserisci_app()
            elif scelta == "2":
                self.modifica_app()
            elif scelta == "3":
                self.agg_invitato()
            elif scelta == "4":
                self.rim_invitato()
            elif scelta == "5":
                self.canc_app()

    def inserisci_app(self):
        descrizione = input("Inserisci descrizione: ")
        data = input("Inserisci data e ora: ") 
        data = datetime.strptime(data, "%Y-%m-%d %H:%M")
        ricorrenza = input("Ricorrenza? ")
        app = Appuntamento(descrizione, data, ricorrenza, [])
        self.appuntamenti.append(app)

    def modifica_app(self):
        #Scelgo l'appuntamento
        mostra_lista(self.appuntamenti)
        a = int(input("Quale appuntamento? "))
        appuntamento = self.appuntamenti[a]
        #Scelgo la descrizione
        appuntamento.descrizione = input("Descrizione? ")
        #Scelgo la data e l'ora
        appuntamento.data_ora = datetime.strptime(input("Data e ora? "), "%Y-%m-%d %H:%M")
        #Scelgo la ricorrenza
        appuntamento.ricorrenza = input("Ricorrenza? ")

    def agg_invitato(self):
        #Scelgo l'appuntamento
        mostra_lista(self.appuntamenti)
        a = int(input("Quale appuntamento? "))
        appuntamento = self.appuntamenti[a]
        nome = input("Nome? ")
        cognome = input("Cognome? ")
        mail = input("Mail? ")
        inv = Invitato(nome, cognome, mail)
        appuntamento.invitati.append(inv)

    def rim_invitato(self):
        #Scelgo l'appuntamento
        mostra_lista(self.appuntamenti)
        a = int(input("Quale appuntamento? "))
        appuntamento = self.appuntamenti[a]
        #Scelgo l'invitato
        mostra_lista(appuntamento.invitati)
        i = int(input("Quale invitato? "))
        appuntamento.invitati.pop(i)

    def canc_app(self):
        #Scelgo l'appuntamento
        mostra_lista(self.appuntamenti)
        a = int(input("Quale appuntamento? "))
        self.appuntamenti.pop(a)

#Main
i1 = Invitato("Alessio", "Grigi", "alessio.grigi@gmail.com")
i2 = Invitato("Michele", "Rossi", "michele.rossi@gmail.com")
i3 = Invitato("Leonardo", "Verdi", "leo.verdi@hotmail.com")
i4 = Invitato("Luca", "Grigi", "l.grigi@alice.it")
i5 = Invitato("Lorenzo", "Arancioni", "lollo.ara@libero.it")
i6 = Invitato("Alessio", "Verdi", "ale.verdi@alice.it")
i7 = Invitato("Alessandro", "Neri", "ale.neri@aruba.it")
i8 = Invitato("Luca", "Fucsia", "luke.fu@gmail.com")

a1 = Appuntamento("Pranzo", datetime.strptime("2023-03-14 12:30", "%Y-%m-%d %H:%M"), "Settimanale", [i1])
a2 = Appuntamento("Riunione", datetime.strptime("2023-07-29 15:10", "%Y-%m-%d %H:%M"), "Annuale", [i2, i3, i4])
a3 = Appuntamento("Dentista", datetime.strptime("2023-12-04 16:45", "%Y-%m-%d %H:%M"), "Mensile", [])
a4 = Appuntamento("Calcetto", datetime.strptime("2023-10-20 14:00", "%Y-%m-%d %H:%M"), "Mensile", [i5, i6, i7])
a5 = Appuntamento("Passeggiata", datetime.strptime("2023-06-13 17:40", "%Y-%m-%d %H:%M"), "Nessuna", [i8])

ag = Agenda([a1, a2, a3, a4, a5])
ag.menu()