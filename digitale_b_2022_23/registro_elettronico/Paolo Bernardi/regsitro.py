from datetime import*

class Appuntamento:
    def _init_(self, descrizione, data_ora, ricorrenza):
        self.descrizione = descrizione
        self.data_ora = data_ora
        self.ricorrenza = ricorrenza

    def _str_(self):
	    return self.descrizione + self.data_ora.strftime("%Y-%m-%d %H:%M:%S") + self.ricorrenza      

class Invitati:
    def _init_(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email

    def _str_(self):
        return f"{self.nome}, {self.cognome}, {self.email}"
class Agenda:
    def _init_(self, appuntamento):
        self.appuntamento = appuntamento

    def menu(self):
        scelta = ""
        while scelta != "6":
            print("1) Inserisci l'apputamento")
            print("2) Modificare la descrizione, la data, l'ora e la ricorrenza di un appuntamento")
            print("3) Aggiungere un invitato ad un appuntamento")
            print("4) Rimuovere un invitato da un appuntamento")
            print("5) Cancellare un appuntamento")
            print("6) Esci")
            scelta = input("Scelta? ")
            if scelta == "1":
                self.modifica_nome_squadra()
            elif scelta == "2":
                self.modifica_anagrafica_calciatore()
            elif scelta == "3":
                self.modifica_forza_calciatore()
            elif scelta == "4":
                self.simula_partita()
            elif scelta =="5":
                pass

    def inserisci_appuntramento(self):
        i = input ("inserisci invitato: ")
        inv = self.invitati[i]
        d = input ("aggiungi descrizione: ")
        des = self.invitati[d]
        do = input ("inserisci data e ora (y-m-d H:M:S): ")
        dtor = self.dat_ora[do]
        r = input ("inserisci riccorenza: ")
        ric = self.riccorenza[r]

