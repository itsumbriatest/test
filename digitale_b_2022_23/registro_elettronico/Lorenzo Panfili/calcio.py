import random

def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Squadra:
    def __init__(self, nome, allenatore, presidente, calciatori) -> None:
        self.nome = nome
        self. allenatore = allenatore
        self.presidente = presidente
        self.calciatori = calciatori
    
    def forza_media(self):
        return sum(c.forza for c in self.calciatori) / len(self.calciatori)#converte la lista giocatori nei loro valori di forza e fa la media

    def __str__(self):
        return self.nome 

class Calciatore:
    def __init__(self, nome, forza, anno) -> None:
        self.nome = nome
        self. forza = forza
        self.anno = anno

    def __str__(self):
        return f"{self.nome}, {self.anno}, {self.forza}" #format string = stringhe dove si sostituiscono le variabili con il loro valore

class Campionato:
    def __init__(self, squadre) -> None:
        self.squadre = squadre

    def menu(self):
        scelta = ""
        while scelta != "5":
            print("1) Modifica nome squadra")
            print("2) Modifica nome calciatore")
            print("3) Modifica anno")
            print("4) Modifica forza")
            print("5) Gioca partita")
            print("6) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.modifica_nomeSq()
            elif scelta == "2":
                self.modifica_nomeC()
            elif scelta == "3":
                self.modifica_anno()
            elif scelta == "4":
                self.modifica_forza()
            elif scelta == "5":
                self.simula_partita()
            
           

    def modifica_nomeSq(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        squadra = self.squadre[s]
        nuovo_nome = input("Inserisci il nuovo nome: ")
        self.squadre[s].nome = nuovo_nome

    def modifica_nomeC(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        Squadra = self.squadre[s]
        mostra_lista(Squadra.calciatori)
        c = int(input("Quale nome vuoi modificare? "))
        calciatore = Squadra.calciatori[c]
        nuovo_nome2 = input("Inserisci il nuovo nome: ")
        Squadra.calciatori[c].nome = nuovo_nome2

    def modifica_anno(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        Squadra = self.squadre[s]
        mostra_lista(Squadra.calciatori)
        c = int(input("Quale calciatore vuoi modificare? "))
        calciatore = Squadra.calciatori[c]
        nuovo_anno = int(input("Inserisci la nuova data: "))
        calciatore.anno = nuovo_anno

    def modifica_forza(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        Squadra = self.squadre[s]
        mostra_lista(Squadra.calciatori)
        c = int(input("Quale calcaitore vuoi modificare? "))
        calciatore = Squadra.calciatori[c]
        nuova_forza = int(input("Inserisci la nuova forza: "))
        if (nuova_forza>0 and nuova_forza<=100):
            Squadra.calciatori[c].forza = nuova_forza
        else:
            print("Parametro non valido")
    
    def simula_partita(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi far giocare? "))
        squadra1 = self.squadre[s]
        forza1 = squadra1.forza_media()
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi far giocare? "))
        squadra2 = self.squadre[s]
        forza2 = squadra2.forza_media()
        goal1 = 0
        goal2 = 0
        for azione in range(5):
            if random.randint(0,100) <= forza1:
                goal1 += 1
            if random.randint(0,100) <= forza2:
                goal2 += 1
        print(f"{squadra1.nome} {goal1} - {goal2} {squadra2.nome}")

#Main
c1 = Calciatore("Franco", 99, 2007)
c2 = Calciatore("Messi", 90, 1989)
c3 = Calciatore("Ibra", 88, 2001)
c4 = Calciatore("Padoin Jr", 72, 2000)

s1 = Squadra("Beverthon", "Pioliisonfire", "Zhang", [c1, c2])
s2 = Squadra("SSSSSlazzzie", "Sarri", "IlCavaliere", [c3, c4])

LigaL = Campionato([s1, s2])
LigaL.menu()