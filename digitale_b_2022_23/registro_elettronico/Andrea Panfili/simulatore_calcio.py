import random


def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Campionato:
    def __init__(self, squadre) -> None:
        self.squadre = squadre

    def menu(self):
        scelta = ""
        while scelta != "5":
            print("1) Modifica nome squadra")
            print("2) Modifica nome calciatore")
            print("3) Modifica anno calciatore")
            print("4) Modifica forza")
            print("5) simula partita")
            print("6) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.nome_squadra()
            elif scelta == "2":
                self.nome_calciatore()
            elif scelta == "3":
                self.anno_calciatore()
            elif scelta == "4":
                self.forza_calciatore()
            elif scelta == "5":
                self.simula_partita()



    def nome_squadra(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        nuovo_nome = input("Inserisci il nuovo nome: ")
        self.squadre[s].nome = nuovo_nome

    def nome_calciatore(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        squadra = self.squadre[s]
        mostra_lista(squadra.calciatori)
        c = int(input("Quale calciatore vuoi modificare? "))
        nuovo_nome2 = input("Inserisci il nuovo nome: ")
        squadra.calciatori[c].nome = nuovo_nome2

    def anno_calciatore(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        squadra = self.squadre[s]
        mostra_lista(squadra.calciatori)
        c = int(input("Quale calciatore vuoi modificare? "))
        nuovo_anno = int(input("Inserisci il nuovo anno: "))
        squadra.calciatori[c].anno = nuovo_anno

    def forza_calciatore(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        squadra = self.squadre[s]
        mostra_lista(squadra.calciatori)
        c = int(input("Quale calciatore vuoi modificare? "))
        nuova_forza = int(input("Inserisci la nuova forza(MIN:1-MAX:100): "))
        if (nuova_forza>0 and nuova_forza<=100):
            squadra.calciatori[c].forza = nuova_forza
        else:
            print("ERRORE!! Nuova forza non valida")

    def simula_partita(self):
        mostra_lista(self.squadre)
        squadra1 = self.squadre[int(input("Squadra 1?"))]
        forza1 = squadra1.forza_media()
        squadra2 = self.squadre[int(input("Squadra 2?"))]
        forza2 = squadra2.forza_media()
        goal1 = 0
        goal2 = 0
        for azione in range(5):
            if random.randint(0, 100) <= forza1:
                goal1 += 1
            if random.randint(0, 100) <= forza2:
                goal2 += 1
        print(f"{squadra1.nome} {goal1} - {goal2} {squadra2.nome}")

class Squadra:
    def __init__(self, nome, presidente, allenatore, calciatori) -> None:
        self.nome = nome
        self.presidente = presidente
        self.allenatore = allenatore
        self.calciatori = calciatori

    def forza_media(self):
        somma = 0
        for g in self.calciatori:
            somma += g.forza
        return somma / len(self.calciatori)
        #return sum(g.forza for g in self.calciatori) / len(self.calciatori)

    def __str__(self) -> str:
        return self.nome 
        
class Calciatore:
    def __init__(self, nome, anno, forza):
        self.nome = nome
        self.anno = anno
        self.forza = forza

    def __str__(self) -> str:
        return f"{self.nome}, {self.anno}, {self.forza}"  #format string


#MAIN

c1 = Calciatore("Andrea", 2003, 80)
c2 = Calciatore("Lorenzo", 2004, 90)
c3 = Calciatore("Massi", 2000, 45)
c4 = Calciatore("Quondy", 2001, 99)
s1 = Squadra("Ternana", "Berlusconi", "Gattuso", [c1, c2])
s2 = Squadra("Perugia", "Moratti", "Pirlo", [c3, c4])
serieB = Campionato([s1, s2])
serieB.menu()


