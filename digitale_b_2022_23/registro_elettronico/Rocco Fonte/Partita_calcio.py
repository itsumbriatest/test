import random

class Campionato:
    def __init__(self, squadre):
        self.squadre = squadre
    
    def menù(self):
        scelta = "0"
        while scelta != "5" :
            print("1) Modifica nome squadra")
            print("2) Modifica nome e anno calciatore")
            print("3) Modifica forza calciatore")
            print("4) Partita fra due squadre")
            print("5) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.modNomeSquadra()
            elif scelta == "2":
                self.modNomeAnnoGiocatore()
            elif scelta == "3":
                self.modForzaGiocatore()
            elif scelta == "4":
                self.partita()

    def stampaSquadre(self):
        i = 0
        for squadra in self.squadre:
            print(i,")", squadra.nome)
            i += 1
    
    def stampaGiocatori(self, squadra):
        i = 0
        for giocatore in squadra.calciatori:
            print(i,")", giocatore.nome, giocatore.anno_nascita, giocatore.forza)
            i += 1

    def modNomeSquadra(self):
        self.stampaSquadre()
        indice = int(input("Scegli squadra: "))
        self.squadre[indice].setNome()

    def modNomeAnnoGiocatore(self):
        self.stampaSquadre()
        indice1 = int(input("Scegli squadra: "))
        sq = self.squadre[indice1]
        self.stampaGiocatori(sq)
        indice2 = int(input("Scegli giocatore: "))
        sq.calciatori[indice2].setNomeAnno()

    def modForzaGiocatore(self):
        self.stampaSquadre()
        indice1 = int(input("Scegli squadra: "))
        sq = self.squadre[indice1]
        self.stampaGiocatori(sq)
        indice2 = int(input("Scegli giocatore: "))
        sq.calciatori[indice2].setPutenza()

    def partita(self):
        rimani = True
        while rimani:
            self.stampaSquadre()
            indice1 = int(input("Scegli la prima squadra: "))
            sq1 = self.squadre[indice1]
            indice2 = int(input("Scegli la seconda squadra: "))
            sq2 = self.squadre[indice2]
            if sq1 != sq2:
                rimani = False
        potenzaSQ1 = sq1.mediaPutenza()
        potenzaSQ2 = sq2.mediaPutenza()
        punteggioSQ1 = 0
        punteggioSQ2 = 0
        for i in range(10):
            gol = random.randint(1,100)
            if i%2 == 0 and potenzaSQ1 >= gol:
                punteggioSQ1 += 1
            elif potenzaSQ2 >= gol:
                punteggioSQ2 += 1
        print(sq1.nome, "\t", sq2.nome)
        print(punteggioSQ1, "\t", punteggioSQ2)



        


class Squadra:
    def __init__(self, nome, presidente, allenatore, calciatori):
        self.nome = nome
        self.presidente = presidente
        self.allenatore = allenatore
        self.calciatori = calciatori

    def setNome(self):
        nome = input("Inserisci il nome della squadra: ")
        self.nome = nome

    def mediaPutenza(self):
        somma = 0
        cont = 0
        for g in self.calciatori:
            somma += g.forza
            cont += 1
        return somma / cont

class Calciatore:
    def __init__(self, nome, anno_nascita, forza):
        self.nome = nome
        self.anno_nascita = anno_nascita
        self.forza = forza #da 0 a 100

    def setNomeAnno(self):
        nome = input("Inserisci un nome: ")
        anno = int(input("Inserisci l'anno di nascita: "))
        self.nome = nome
        self.anno_nascita = anno

    def setPutenza(self):
        rimani = True
        while rimani:
            f = input("Inserisci la forza: ")
            if f.isdigit():
                forza = int(f)
                if forza >= 0 and forza <= 100:
                    self.forza = forza
                    rimani = False
                else:
                    print("Devi inserire un numero tra 0 e 100")
            else:
                print("Devi inserire un numero")

#MAIN

c1 = Calciatore("Arancina",2000,100)
c2 = Calciatore("Pizza",2000,85)
c3 = Calciatore("Lasagna",2000,75)
c4 = Calciatore("Gelato",2000,80)
c5 = Calciatore("Torta",2000,90)
c6 = Calciatore("Genovese",2000,60)
s1 = Squadra("Salato","a","a",[c1,c2,c3])
s2 = Squadra("Dolce","b","b",[c4,c5,c6])
camp = Campionato([s1,s2])
camp.menù()
