from datetime import *

def mostra_oggetti(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Invitato:
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
    
    def __str__(self):
        return f"{self.nome} {self.cognome} <{self.email}>"

class Appuntamento:
    def __init__(self, descrizione, data_e_ora, ricorrenza):
        self.descrizione = descrizione
        self.data_e_ora = data_e_ora
        self.ricorrenza = ricorrenza
        self.invitati = []
    
    def __str__(self):
        do = self.data_e_ora.strftime("%Y-%m-%d %H:%M")
        return f"{do}: {self.descrizione}"

class Agenda:
    def __init__(self):
        self.appuntamenti = []
    
    def menu(self):
        scelta = ""
        while scelta != "6":
            print("1) Nuovo appuntamento")
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
            elif scelta == "5":
                self.cancella_appuntamento()
    
    def nuovo_appuntamento(self):
        descrizione = input("Descrizione: ")
        data = input("Data (AAAA-MM-GG): ")
        ora = input("Ora (OO:MM): ")
        ricorrenza = ("Ricorrenza: ")
        data_e_ora = datetime.strptime(f"{data} {ora}", "%Y-%m-%d %H:%M")
        app = Appuntamento(descrizione, data_e_ora, ricorrenza)
        self.appuntamenti.append(app)
    
    def modifica_appuntamento(self):
        mostra_oggetti(self.appuntamenti)
        a = int(input("Indice appuntamento: "))
        app = self.appuntamenti[a]
        app.descrizione = input("Descrizione: ")
        data = input("Data (AAAA-MM-GG): ")
        ora = input("Ora (OO:MM): ")
        app.data_e_ora = datetime.strptime(f"{data} {ora}", "%Y-%m-%d %H:%M")
        app.ricorrenza = ("Ricorrenza: ")
    
    def aggiungi_invitato(self):
        mostra_oggetti(self.appuntamenti)
        a = int(input("Indice appuntamento: "))
        app = self.appuntamenti[a]
        inv = Invitato(input("Cognome: "), input("Nome: "), input("Email: "))
        app.invitati.append(inv)
    
    def rimuovi_invitato(self):
        mostra_oggetti(self.appuntamenti)
        a = int(input("Indice appuntamento: "))
        app = self.appuntamenti[a]
        mostra_oggetti(app.invitati)
        i = int(input("Indice invitato: "))
        app.invitati.pop(i)

    def cancella_appuntamento(self):
        mostra_oggetti(self.appuntamenti)
        a = int(input("Indice appuntamento: "))
        self.appuntamenti.pop(a)

# Main code
agenda = Agenda()
agenda.menu()