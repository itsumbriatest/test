import random


def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1


class Squadra:
    def __init__(self, nome, presidente, allenatore, calciatori):
       self.nome = nome
       self.presidente = presidente
       self.allenatore = allenatore
       self.calciatori = calciatori
   
    def __str__(self):
        return self.nome 
    
    def forza_media(self):
	    return sum(c.forza for c in self.calciatori) / len(self.calciatori)

class Calciatore:
    def __init__(self, nome, forza, annoN):
        self.nome = nome
        self.forza = forza
        self.annoN = annoN

    def __str__(self):
        return self.nome  
    


class Campionato:
    def __init__(self, squadre):
        self.squadre = squadre

    def menu(self):

        scelta = ""
        while scelta != "5":
            print("1) Cambia il nome di una squadra")
            print("2) Cambia il nome di un giocatore")
            print("3) Cambia l'anno di un giocatore")
            print("4) Modifica forza")
            print("5) Gioca la partita")
            print("6) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.cNSquadra()
            elif scelta == "2":
                self.cambia_giocatore()
            elif scelta == "3":
                self.cambia_anno()
            elif scelta == "4":
                self.modifica_forza()
            elif scelta == "5":
                self.gioca_partita()

           
    def cNSquadra(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi modificare? "))
        squadra = self.squadre[s]
        nuovo_nome = input("Quale nuovo nome vuoi inserire? ")
        squadra.nome = nuovo_nome
    
    def cambia_giocatore(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi scegliere? "))
        squadra = self.squadre[s]
        mostra_lista(squadra.calciatori)
        c = int(input("Quale calciatore vuoi scegliere? "))
        calciatore = squadra.calciatori[c]
        nuovo_nome2 = input("Quale nome vuoi inserire? ")
        calciatore.nome = nuovo_nome2
    
    def cambia_anno(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi scegliere? "))
        squadra = self.squadre[s]
        mostra_lista(squadra.calciatori)
        c = int(input("Quale calciatore vuoi scegliere? "))
        calciatore = squadra.calciatori[c]
        nuovo_anno = int(input("Inserisci la nuova data di nascita "))
        calciatore.annoN = nuovo_anno

    def modifica_forza(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi scegliere? "))
        squadra = self.squadre[s]
        mostra_lista(squadra.calciatori)
        c = int(input("Quale calciatore vuoi scegliere? "))
        calciatore = squadra.calciatori[c]
        nuova_forza = int(input("Inserisci la nuova forza "))
        if (nuova_forza <= 100 and nuova_forza >= 1):
            calciatore.forza = nuova_forza
        else:
            print("Hai inserito un valore non valido ")


    def gioca_partita(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra vuoi far giocare? "))
        squadra1 = self.squadre[s]
        forza1 = squadra1.forza_media()  
        mostra_lista(self.squadre)
        s = int(input("Scegli la seconda squadra "))
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
    
    
    #def simula_partita(self):
    #    mostra_lista(self.squadre)
	#    squadra1 = self.squadre[int(input("Squadra 1? "))]
	#	forza1 = squadra1.forza_media()
	#	squadra2 = self.squadre[int(input("Squadra 2? "))]
	#	forza2 = squadra2.forza_media()
	#	goal1 = 0
	#	goal2 = 0
	#	# 5 azioni a testa, le faccio contemporaneamente
	#	for azione in range(5):
	#		if random.randint(0, 100) <= forza1:
	#			goal1 += 1
	#		if random.randint(0, 100) <= forza2:
	#			goal2 += 1
	#	print(f"{squadra1.nome} {goal1} - {goal2} {squadra2.nome}")
        

        
        

        



 






c1 = Calciatore("Massimiliano Muzi", 45, 2003)
c2 = Calciatore("Franco Bo", 78, 2007)
c3 = Calciatore("spanky Polverij", 18, 1998)
c4 = Calciatore("Mattia Ruco", 68, 2005)
s1 = Squadra("Pipponi", "Stino", "Piovra", [c1, c2])
s2 = Squadra("Scarsoni", "Mino", "Gentili", [c3, c4])
 
serieD = Campionato([s1, s2]) 
d = serieD    
d.menu()   