from datetime import *

class agenda:
    def __init__(self, appuntamenti):
        self.appuntamenti=appuntamenti

    def menu(self):
        scelta = 0
        while scelta != "6":
            print("menu")
            print("---------------------")
            print("1) inserisci appuntamento")
            print("2) modifica appuntamento")
            print("3) aggiungi invitato")
            print("4) rimuovi invitato")
            print("5) cancella appuntamento")
            print("6) esci")
            scelta = input("scelta? ")
            if scelta == "1":
                self.inserisci_app()
            elif scelta == "2":
                self.modifica_app()
            elif scelta == "3":
                self.aggiungi_inv()  
            elif scelta == "4":
                self.rimuovi_inv()
            elif scelta == "5":
                self.cancella_app()

    def mostra_appuntamenti(self):
        i = 0
        for appuntamento in self.appuntamenti:
            print(i, appuntamento.descrizione, appuntamento.data_e_ora, appuntamento.ricorrenza, appuntamento.invitati)
            i = i + 1

    def mostra_invitati(self, appuntamento):
        i = 0
        for invitato in appuntamento.invitati:
            print(i, invitato.nome, invitato.cognome, invitato.email)
            i = i + 1

    def inserisci_app(self):
        descrizione = input("inserire descrizione: ")
        data = input("inserire data (aaaa-mm-gg): ")
        ora = input("inserire orario (oo:mm): ")
        ricorrenza = input("inserire una ricorrenza: ")
        app = appuntamento(descrizione, data, ora, ricorrenza, [])
        self.appuntamenti.append(app)

    def modifica_app(self):
        self.mostra_appuntamenti()
        f= int(input("quale appuntamento? "))
        nuova_descrizione = input("inserire descrizione:? ")
        nuova_data = input("inserire data (aaaa-mm-gg): ")
        nuova_ora = input("inserire orario (oo:mm): ")
        nuova_ricorrenza = input("inserire una ricorrenza: ")
        self.appuntamenti[f].descrizione = nuova_descrizione
        self.appuntamenti[f].data = nuova_data
        self.appuntamenti[f].ora = nuova_ora
        self.appuntamenti[f].ricorrenza = nuova_ricorrenza

    def aggiungi_inv(self):
        self.mostra_appuntamenti()
        f= int(input("quale appuntamento? "))
        appuntamento = self.appuntamenti[f]
        nome = input("inserire nome: ")
        cognome = input("inserire cognome: ")
        email = input("inserire email: ")
        inv = invitato(nome, cognome, email)
        appuntamento.invitati.append(inv)

    def rimuovi_inv(self):
        self.mostra_appuntamenti()
        f= int(input("quale appuntamento? "))
        appuntamento = self.appuntamenti[f]
        self.mostra_invitati(appuntamento)
        inv= int(input("quale invitato? "))
        appuntamento.invitati.pop(inv)

    def cancella_app(self):
        self.mostra_appuntamenti()
        f= int(input("quale appuntamento? "))
        self.appuntamenti.pop(f)


class appuntamento:
    def __init__(self, descrizione, data, ora, ricorrenza, invitati):
        self.descrizione=descrizione
        data_e_ora = datetime.strptime(data + " " + ora, "%Y-%m-%d %H:%M")
        self.data_e_ora=data_e_ora
        self.ricorrenza=ricorrenza
        self.invitati=invitati

    def __str__(self):
        return self.descrizione + " " + self.data_e_ora + " " + self.ricorrenza + " " + self.invitati

class invitato:
    def __init__(self, nome, cognome, email):
        self.nome=nome
        self.cognome=cognome
        self.email=email
    
    def __str__(self):
        return self.nome + " " + self.cognome + " " + self.email
    
    def __repr__(self):
        return str(self)

#main
i1=invitato("gino", "rossi", "g.rossi@ttytutu.it")
i2=invitato("paolo", "neri", "p.neri@yfyury.it")
i3=invitato("ugo", "bianchi", "u.bianchi@hmsyrs.it")
i4=invitato("alberto", "verdi", "a.verdi@uyiuiut.it")
a1=appuntamento("cena nonna", "2023-03-20", "19:30", "settimanale", [])
a2=appuntamento("conferenza", "2023-03-31", "15:00", "nessuna", [i1])
a3=appuntamento("dentista", "2023-04-10", "18:15", "mensile", [i2])
a4=appuntamento("ufficio", "2023-03-14", "08:30", "giornaliera", [i3, i4])
ag=agenda([a1, a2, a3, a4])
ag.menu()