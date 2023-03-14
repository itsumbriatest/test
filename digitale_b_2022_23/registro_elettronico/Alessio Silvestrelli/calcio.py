import random

class campionato:
    def __init__(self, squadre):
        self.squadre=squadre

    def menu(self):
        scelta = 0
        while scelta != "5":
            print("menu")
            print("---------------------")
            print("1) modifica nome squadra")
            print("2) modifica nome e anno giocatore")
            print("3) modifica forza giocatore")
            print("4) simula partita")
            print("5) esci")
            scelta = input("scelta? ")
            if scelta == "1":
                self.modifica_squadra()
            elif scelta == "2":
                self.modifica_giocatore()
            elif scelta == "3":
                self.modifica_forza()  
            elif scelta == "4":
                self.simula()

    def mostra_squadra(self):
        i = 0
        for squadra in self.squadre:
            print(i, squadra.nome, squadra.presidente, squadra.allenatore, squadra.giocatori)
            i = i + 1

    def mostra_giocatore(self, squadra):
        i = 0
        for giocatore in squadra.giocatori:
            print(i, giocatore.nome, giocatore.anno, giocatore.forza)
            i = i + 1

    def modifica_squadra(self):
        self.mostra_squadra()
        f= int(input("quale squadra? "))
        nuovo_nome = input("quale nome? ")
        self.squadre[f].nome = nuovo_nome

    def modifica_giocatore(self):
        self.mostra_squadra()
        f= int(input("quale squadra? "))
        self.mostra_giocatore(self.squadre[f])
        g= int(input("quale giocatore? "))
        nuovo_nome = input("quale nome? ")
        nuova_data = input("quale anno?")
        self.squadre[f].giocatori[g].nome = nuovo_nome
        self.squadre[f].giocatori[g].anno = nuova_data

    def modifica_forza(self):
        self.mostra_squadra()
        f= int(input("quale squadra? "))
        self.mostra_giocatore(self.squadre[f])
        h= int(input("quale giocatore? "))
        nuova_forza = input("quale forza? ")
        if h<1 or h>99:
            print("valore non valido")
        else:
            self.squadre[f].giocatori[h].forza = nuova_forza

    def simula(self):
        scegli=True
        while(scegli):
            self.mostra_squadra()
            a= int(input("squadra 1?"))
            sq1=self.squadre[a]
            b= int(input("squadra 2?"))
            sq2=self.squadre[b]
            if sq1!=sq2:
                scegli=False
        forza_sq1= sq1.media_forza()
        forza_sq2= sq2.media_forza()
        gol_sq1=0
        gol_sq2=0
        for i in range(10):
            gol=random.randint(1, 100)
            if i%2 and forza_sq1 >= gol:
                gol_sq1+=1
            elif forza_sq2 >= gol:
                gol_sq2 +=1
        print(sq1.nome, "\t", sq2.nome)
        print(gol_sq1, "\t", gol_sq2)
        if(gol_sq1>gol_sq2):
            print("vince la squadra locale!")
        elif(gol_sq2>gol_sq1):
            print("vince la squadra ospite!")
        else:
            print("pareggio!")





class squadra:
    def __init__(self, nome, presidente, allenatore, giocatori):
        self.nome=nome
        self.presidente=presidente
        self.allenatore=allenatore
        self.giocatori=giocatori

    def media_forza(self):
        somma = 0
        for giocatore in self.giocatori:
            somma += giocatore.forza
        return somma / len(self.giocatori)
    
    def __str__(self):
        return self.nome + " " + self.presidente + " " + self.allenatore 

class giocatore:
    def __init__(self, nome, anno, forza):
        self.nome=nome
        self.anno=anno
        self.forza=forza
    
    def __str__(self):
        return self.nome + " " + str(self.anno) + " " + str(self.forza)
    
    def __repr__(self):
        return str(self)

# main
g1=giocatore("cristiano ronado", "1985", 90)
g2=giocatore("kevin de bruyne", "1991", 89)
g3=giocatore("giorgio chiellini", "1983", 84)
g4=giocatore("lionel messi", "1987", 91)
g5=giocatore("paul pogba", "1992", 85)
g6=giocatore("sergio ramos", "1986", 83)
g7=giocatore("antoine griezmann", "1991", 86)
g8=giocatore("sergej milinkovic-savic", "1985", 87)
g9=giocatore("danilo", "1990", 84)
s1=squadra("juve", "agnelli", "allegri", [g1, g2, g3])
s2=squadra("inter", "zhang", "inzaghi", [g4, g5, g6])
s3=squadra("milan", "elliot", "pioli", [g7, g8, g9])
c=campionato([s1, s2, s3])
c.menu()