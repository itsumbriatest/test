from datetime import *

def mostra_oggetti(oggetti):
	i = 0
	for o in oggetti:
		print(i, o)
		i += 1
		
class Appuntamenti:
	def __init__(self, descrizione, data, ora, ricorreza, invitati):
		self.descrizione = descrizione
		self.data = data
		self.ora = ora
		self.ricorrenza = ricorreza
		self.invitati = invitati
	
	def __str__(self):
		return f"{self.descrizione}, {self.data}, {self.ora}, {self.ricorrenza}"
	
class Invitati:
	def __init__(self, nome, cognome, mail):
		self.nome = nome
		self.cognome = cognome
		self.mail = mail
	
	def __str__(self):
		return f"{self.nome}, {self.cognome}, {self.mail}"
	
class Agenda:
    def __init__(self, listAp): 
        self.listAp = listAp
    
    def menu(self):
        scelta = ""
        while scelta != "9":
            print("1) Nuovo appuntamento")
            print("2) Modifica descrizione")
            print("3) Modifica data")
            print("4) Modifica l'ora")
            print("5) Modifica ricorrenza")
            print("6) Aggiungere nuovo invitato")
            print("7) Rimuovi invitato")
            print("8) Cancella appuntamento")
            print("9) Esci")
            scelta = input("Scelta? ")
            if scelta == "1":
                self.crea_nuovo_appuntamento()
            elif scelta == "2":
                self.modifica_descrizione()
            elif scelta == "3":
                self.modifica_data()
            elif scelta == "4":
                self.modifica_ora()
            elif scelta == "5":
                self.modifica_ricorreza()
            elif scelta == "6":
                self.aggiungi_nuovo_invitato()
            elif scelta == "7":
                self.rimuovi_invitato()
            elif scelta == "8":
                self.cancella_appuntamento()

    def crea_nuovo_appuntamento(self):
        mostra_oggetti(self.listAp)
        desc = input("Inserisci descrizione: ")
        dat = input("Inserisci data: ")
        ora = input("Inserisci ora: ")
        ric = input("Inserisci ricorrenza: ")
        inv = input("Inserisci invitato/i: ")
        appunt = Appuntamenti(desc, dat, ora, ric, inv)
        self.listAp.append(appunt)

    def modifica_descrizione(self):
        mostra_oggetti(self.listAp)
        desc = int(input("Descrizione? "))
        self.listAp[desc].descrip = input("Nuova descrizione? ")
        
    def modifica_data(self):
        mostra_oggetti(self.listAp)
        dat = int(input("Data? "))
        self.listAp[dat].data = input("Nova data? ")

    def modifica_ora(self):
        mostra_oggetti(self.listAp)
        ora = int(input("Ora? "))
        self.listAp[ora].orario = input("Novo orario? ")
    
    def modifica_ricorreza(self):
        mostra_oggetti(self.listAp)
        ric = int(input("Ricorrenza? "))
        self.listAp[ric].ricorrenza = input("Nuova ricorrenza? ")
    
    def aggiungi_nuovo_invitato(self):
        mostra_oggetti(self.listAp)
        nom = input("nome: ")
        cogn = input("cognome: ")
        mail = input("mail: ")
        inv = Invitati(nom, cogn, mail)
        self.listAp.append(inv)
        
    def rimuovi_invitato(self):
        mostra_oggetti(self.listAp)
        input

    
    def cancella_appuntamento(self):
        mostra_oggetti(self.listAp)
        appunt = input("Vuoi cancellare l'appuntamento? ")

        self.listAp.pop(appunt)

agg = Agenda([])
agg.menu()


            

