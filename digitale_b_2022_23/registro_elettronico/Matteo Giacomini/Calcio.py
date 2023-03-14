import random

def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Squadre:
    def __init__(self, nome, presidente, allenatore, calciatori):
        self.nome = nome
        self.presidente = presidente
        self.allenatore = allenatore
        self.calciatori = calciatori

    def forza_media(self):
        return sum(g.forza for g in self.calciatori) / len(self.calciatori)

    def __str__(self):
        return self.nome

class Calciatori:
    def __init__(self, nome, anno_nascita, forza):
        self.nome = nome
        self.anno_nascita = anno_nascita
        self.forza = forza

    def __str__(self):
        return self.nome + "(" + str(self.anno_nascita) + ")" + "(" + str(self.forza) + ")"

class Campionato:
    def __init__(self, squadre):
        self.squadre = squadre

    def menu(self):
        scelta = ""
        while scelta != "5":
            print("1- Modifica nome di una squadra")
            print("2- Modifica nome e anno di nascita di un giocatore")
            print("3- Modifica forza di un calciatore")
            print("4- Simula partita")
            print("5- Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.modifica_nomes()
            elif scelta == "2":
                self.modifica_nome_annoc()
            elif scelta == "3":
                self.modifica_forza()
            elif scelta == "4":
                self.simula_partita()

    def modifica_nomes(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra? "))
        nuovo_nomes = input("Nuovo nome: ")
        self.squadre[s].nome = nuovo_nomes

    def modifica_nome_annoc(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra? "))
        mostra_lista(self.squadre[s].calciatori)
        c = int(input("Quale calciatore? "))
        calc = self.squadre[s].calciatori[c]
        calc.nome = input("Nuovo nome: ")
        calc.anno_nascita = int(input("Nuovo anno di nascita: "))

    def modifica_forza(self):
        mostra_lista(self.squadre)
        s = int(input("Quale squadra? "))
        mostra_lista(self.squadre[s].calciatori)
        c = int(input("Quale calciatore? "))
        f = self.squadre[s].calciatori[c]
        f.forza = int(input("Inserisci la nuova forza (compresa tra 0 e 100): "))
        while f.forza < 0 or f.forza > 100:
            f.forza = int(input("Inserisci la nuova forza (compresa tra 0 e 100): "))

    def simula_partita(self):
        mostra_lista(self.squadre)
        squadra1 = self.squadre[int(input("Squadra 1? "))]
        forza1 = squadra1.forza_media()
        squadra2 = self.squadre[int(input("Squadra 2? "))]
        forza2 = squadra2.forza_media()
        goal1 = 0
        goal2 = 0
		# 5 azioni a testa, le faccio contemporaneamente
        for azione in range(5):
            if random.randint(0, 100) <= forza1:
                goal1 += 1
            if random.randint(0, 100) <= forza2:
                goal2 += 1
        print(f"{squadra1.nome} {goal1} - {goal2} {squadra2.nome}")

kkk = Calciatori("KKK", 1865, 100)
ll = Calciatori("LuLupo", 1980, 18)
ca = Calciatori("Ctrl C/Ctrl V", 1983, 50)
exe = Calciatori("EXE", 1972, 69)
tor = Calciatori("Tor", 1982, 100)
bimbi = Calciatori("Leo", 2000, 90)
psg = Squadre("PSG", "Michael", "Bizzarri", [ll, bimbi])
alatri = Squadre("Alatri", "Giorgio", "Cittadini", [tor, ca])
napoli = Squadre("Napoli", "Manuel", "Pagliarulo", [kkk, exe])
c = Campionato([psg, alatri, napoli])
c.menu()