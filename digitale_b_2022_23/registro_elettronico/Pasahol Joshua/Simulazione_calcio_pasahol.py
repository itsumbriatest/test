import random

class Campionato:
    def __init__(self, squadra):
        self.squadre = squadra
    def menu(self):
        scelta = ""
        while scelta != "5":
            print("1) Modificare il nome di una squadra")
            print("2) Modificare il nome e anno di nascita di un calciatore")
            print("3) Modifica la forza di un calciotore")
            print("4) Fare una simulazione")
            print("5) Per EXIT")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.modifica_Squadra()
            elif scelta == "2":
                self.modifica_Calciatore()
            elif scelta == "3":
                self.modifca_Forza()
            elif scelta == "4":
                pass
    
    def mostra_Squadra(self):
        i = 0
        for squadra in self.squadre:
            print(i, squadra.nome, squadra.presidente, squadra.allenatore, squadra.calciatori)
            i += 1

    def mostra_Calciatori(self, squadra):
        i = 0
        for calciatore in squadra.calciatori:
            print(i, calciatore.nome, calciatore.anno, calciatore.forza)
            i += 1

    def modifica_Squadra(self):
        #scelgo la squadra
        self.mostra_Squadra()
        s = int(input("Quale squadra? "))
        nuovo_nome = input("quale nome: ")
        self.squadre[s].nome = nuovo_nome
        print("Il nuovo nome della squadra è: ", nuovo_nome)
    
    def modifica_Calciatore(self):
        self.mostra_Squadra()
        s = int(input("Quale squadra? "))
        self.mostra_Calciatori(self.squadre[s])
        c = int(input("Quale calciatore? "))
        nuovo_nome = input("quale nome? ")
        nuovo_anno = input("Quale anno? ")
        self.squadre[s].calciatore[c].nome = nuovo_nome
        self.squadre[s].calciatore[c].anno = nuovo_anno
        print("Il nuovo nome è: ", nuovo_nome)
        print("Il nuovo anno è: ", nuovo_anno)

    def modifca_Forza(self):
        self.mostra_Squadra()
        s = int(input("Quale squadra? "))
        self.mostra_Calciatori(self.squadre[s])
        c = int(input("Quale calciatore? "))
        nuova_forza = input("Quale forza? ")
        if nuova_forza < "0" or nuova_forza > "100":
            print("Riprova")
        else:
            self.squadre[s].calciatore[c].forza = nuova_forza
            print("La nuova forza è: ", nuova_forza)
class Squadre:
    def __init__(self, nome, presidente, allenatore, calciatori):
        self.nome = nome
        self.presidente = presidente
        self.allenatore = allenatore
        self.calciatori = calciatori
    def __str__(self):
        return self.nome + " " + self.presidente + " " + self.allenatore + " " + self.calciatori

class Calciatore:
    def __init__(self, nome, anno, forza):
        self.nome = nome
        self.anno = anno
        self.forza = forza
    def __str__(self):
        return self.nome + " " + self.anno + " " + str(self.forza)
    def __repr__(self):
        return str(self)

#main
c1 = Calciatore("Bianco", "20/11/1992", 88)
c2 = Calciatore("Nero", "06/12/1982", 98)
c3 = Calciatore("Verde", "02/02/1984", 85)
c4 = Calciatore("Blu", "15/04/1987", 80)
g1 = Calciatore("Gelato", "13/11/1985", 97)
g2 = Calciatore("Pizza", "08/11/1983", 89)
g3 = Calciatore("Pasta", "22/11/1990", 81)
g4 = Calciatore("Riso", "29/02/1987", 94)
s1 = Squadre("ff1", "Viola", "Blu", [c1, c2, c3, c4])
s2 = Squadre("ff2", "Meloni", "Arancia", [g1, g2, g3, g4])
t = Campionato([s1, s2])
t.menu()