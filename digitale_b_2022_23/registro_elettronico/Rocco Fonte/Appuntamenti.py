from datetime import *

class Agenda:
    def __init__(self, appuntamenti):
        self.appuntamenti = appuntamenti
    
    def menù(self):
        scelta = "0"
        while scelta != "6" :
            print("1) Aggiungi un appuntamento")
            print("2) Modifica un appuntamento")
            print("3) Aggiungi un invitato")
            print("4) Rimuovi un invitato")
            print("5) Cancella un appuntamento")
            print("6) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.aggiungiAppuntamento()
            elif scelta == "2":
                self.modificaAppuntamento()
            elif scelta == "3":
                self.aggiungiInvitato()
            elif scelta == "4":
                self.rimuoviInvitato()
            elif scelta == "5":
                self.cancellaAppuntamento()
    
    def stampaAppuntamenti(self):
        i = 0
        for a in self.appuntamenti:
            print(i,")", a.descrizione)
            i += 1
    
    def stampaInvitati(self, appuntamento):
        i = 0
        for inv in appuntamento.invitati:
            print(i,")", inv.nome, inv.cognome)
            i += 1

    def aggiungiAppuntamento(self):
        desc = input("Inserisci descrizione: ")
        d = input("Insersici data e ora: ")
        data = datetime.strptime(d,"%Y-%m-%d %H:%M:%S")
        rimani = True
        while rimani:
            ric = int(input("Inserisci ricorrenza:\n0)Nessuna\n1)Giornaliera\n2)Settimanale\n3)Annuale\n"))
            if ric >= 0 and ric <= 3:
                rimani = False 
        nuovo_appunt = Appuntamento(desc, data, ric, [])
        self.appuntamenti.append(nuovo_appunt)

    def modificaAppuntamento(self):
        self.stampaAppuntamenti()
        risp1 = int(input("Quale appuntamento vuoi modificare? "))
        print("Cosa vuoi modificare?")
        print("1) Descrizione")
        print("2) Data e Ora")
        print("3) Ricorrenza")
        risp2 = input()
        if risp2 == "1":
            self.appuntamenti[risp1].setDescrizione()
        elif risp2 == "2":
            self.appuntamenti[risp1].setDataOra()
        elif risp2 == "3":
            self.appuntamenti[risp1].setRicorrenza()
    
    def aggiungiInvitato(self):
        self.stampaAppuntamenti()
        risp = int(input("Quale appuntamento vuoi modificare? "))
        nome = input("Inserisci nome dell'invitato: ")
        cognome = input("Inserisci cognome dell'invitato: ")
        email = input("Inserisci email dell'invitato: ")
        inv = Invitati(nome, cognome, email)
        self.appuntamenti[risp].invitati.append(inv)
        
    def rimuoviInvitato(self):
        self.stampaAppuntamenti()
        risp1 = int(input("Quale appuntamento vuoi modificare? "))
        self.stampaInvitati(self.appuntamenti[risp1])
        risp2 = int(input("Quale invitato vuoi rimuovere? "))
        inv = self.appuntamenti[risp1].invitati[risp2]
        self.appuntamenti[risp1].invitati.remove(inv)

    def cancellaAppuntamento(self):
        self.stampaAppuntamenti()
        risp = int(input("Quale appuntamento vuoi cancellare? "))
        app = self.appuntamenti[risp]
        self.appuntamenti.remove(app)


    
class Appuntamento:
    def __init__(self, descrizione, data, ricorrenza, invitati):
        self.descrizione = descrizione
        self.data = data #data e ora
        self.ricorrenza = ricorrenza #0, 1, 2, 3
        self.invitati = invitati #0 o più invitati

    def setDescrizione(self):
        self.descrizione = input("Inserisci descrizione: ")
    
    def setDataOra(self):
        d = input("Inserisci la nuova data: ")
        self.data = datetime.strptime(d,"%Y-%m-%d %H:%M:%S")

    def setRicorrenza(self):
        rimani = True
        while rimani:
            ric = int(input("Inserisci ricorrenza:\n0)Nessuna\n1)Giornaliera\n2)Settimanale\n3)Annuale\n"))
            if ric >= 0 and ric <= 3:
                rimani = False

class Invitati:
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email

# MAIN
    
ag = Agenda([])
ag.menù()