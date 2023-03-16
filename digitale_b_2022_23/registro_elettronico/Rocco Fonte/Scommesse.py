class Agenzia:
    def __init__(self,lista_sport):
        self.lista_sport = lista_sport

    def menu(self):
        scelta = "0"
        while scelta != "7" :
            print("1) Aggiungi uno sport")
            print("2) Rimuovi uno sport")
            print("3) Aggiungi una scommessa")
            print("4) Rimuovi una scommessa")
            print("5) Risultato di una scommessa")
            print("6) Scommesse totali")
            print("7) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.aggiungiSport()
            elif scelta == "2":
                self.rimuoviSport()
            elif scelta == "3":
                self.aggiungiScommessa()
            elif scelta == "4":
                self.rimuoviScommessa()
            elif scelta == "5":
                self.risultatoScommessa()
            elif scelta == "6":
                self.scommTotali()

    def stampaSport(self):
        i = 0
        for sport in self.lista_sport:
            print(i,")", sport.nome)
            i += 1
    
    def stampaScommesse(self, sport):
        i = 0
        for scom in sport.lista_scomm:
            print(i,")", scom.descrizione)
            i += 1

    def stampaOpzioni(self, scommessa):
        i = 0
        for op in scommessa.lista_opt:
            print(i,")", op.vincita)
            i += 1

    def aggiungiSport(self):
        self.stampaSport()
        nome = input("Inserisci nome: ")
        s = Sport(nome, [])
        self.lista_sport.append(s)

    def rimuoviSport(self):
        self.stampaSport()
        indice = int(input("Quale sport vuoi rimuovere? "))
        self.lista_sport.pop(indice)

    def aggiungiScommessa(self):
        self.stampaSport()
        indice = int(input("A quale sport vuoi aggiungere una scommessa? "))
        descrizione = input("Inserisci descrizione: ")
        vincita = input("Inserisci la vincita dell'opzione: ")
        risultato = input("Inserisci risultato: ")
        scomm = Scommesse(descrizione, [Opzioni(vincita)], risultato)
        self.lista_sport[indice].lista_scomm.append(scomm)
    
    def rimuoviScommessa(self):
        self.stampaSport()
        indice1 = int(input("A quale sport vuoi rimuovere una scommessa? "))
        self.stampaScommesse(self.lista_sport[indice1])
        indice2 = int(input("Quale scommessa vuoi rimuovere? "))
        self.lista_sport[indice1].lista_scomm.pop(indice2)

    def risultatoScommessa(self):
        self.stampaSport()
        indice1 = int(input("Di quale sport vuoi vedere il risultato? "))
        self.stampaScommesse(self.lista_sport[indice1])
        indice2 = int(input("Di quale scommessa vuoi vedere il risultato? "))
        r = self.lista_sport[indice1].lista_scomm[indice2].risultato
        print("Risultato:", r)

    def scommTotali(self):
        cont = 0
        for sport in self.lista_sport:
            cont += len(sport.lista_scomm)
        print("Ci sono", cont, "scommesse")

class Sport:
    def __init__(self, nome, lista_scomm):
        self.nome = nome
        self.lista_scomm = lista_scomm

class Scommesse:
    def __init__(self, descrizione, lista_opt, risultato):
        self.descrizione = descrizione
        self.lista_opt = lista_opt
        self.risultato = risultato

class Opzioni:
    def __init__(self, vincita):
        self.vincita = vincita

#MAIN
a1 = Agenzia([])
a1.menu()