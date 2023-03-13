import random

def mostra_oggetti(oggetti):
	for i, o in enumerate(oggetti):
		print(i, o)

class Giocatore:
	def __init__(self, nome, anno, forza):
		self.nome = nome
		self.anno = anno
		self.forza = forza
	
	def __str__(self):
		return f"{self.nome}, {self.anno}, {self.forza}"

class Squadra:
	def __init__(self, nome, allenatore, presidente, giocatori):
		self.nome = nome
		self.allenatore = allenatore
		self.presidente = presidente
		self.giocatori = giocatori
	
	def forza_media(self):
		return sum(g.forza for g in self.giocatori) / len(self.giocatori)

	def __str__(self):
		return self.nome

class Campionato:
	def __init__(self, squadre):
		self.squadre = squadre
	
	def menu(self):
		scelta = ""
		while scelta != "5":
			print("1) Modifica nome squadra")
			print("2) Modifica anagrafica calciatore")
			print("3) Modifica forza calciatore")
			print("4) Simula partita")
			print("5) Esci")
			scelta = input("Scelta? ")
			if scelta == "1":
				self.modifica_nome_squadra()
			elif scelta == "2":
				self.modifica_anagrafica_calciatore()
			elif scelta == "3":
				self.modifica_forza_calciatore()
			elif scelta == "4":
				self.simula_partita()
	
	def modifica_nome_squadra(self):
		mostra_oggetti(self.squadre)
		s = int(input("Squadra? "))
		self.squadre[s].nome = input("Nuovo nome? ")
	
	def modifica_anagrafica_calciatore(self):
		mostra_oggetti(self.squadre)
		s = int(input("Squadra? "))
		mostra_oggetti(self.squadre[s].giocatori)
		g = int(input("Giocatore? "))
		self.squadre[s].giocatori[g].nome = input("Nuovo nome? ")
		self.squadre[s].giocatori[g].anno = int(input("Nuovo anno di nascita? "))

	def modifica_forza_calciatore(self):
		mostra_oggetti(self.squadre)
		s = int(input("Squadra? "))
		mostra_oggetti(self.squadre[s].giocatori)
		g = int(input("Giocatore? "))
		forza = int(input("Nuova forza? "))
		while forza < 0 or forza > 100:
			forza = int(input("Nuova forza (0-100)? "))
		self.squadre[s].giocatori[g].forza = forza
	
	def simula_partita(self):
		mostra_oggetti(self.squadre)
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

# Main code
g1 = Giocatore("Pino", 1892, 60)
g2 = Giocatore("Luigi", 1891, 72)
g3 = Giocatore("Gianni", 1892, 88)
g4 = Giocatore("Ezio", 1891, 52)
s1 = Squadra("Fiorentina", "Paolo", "Andrea", [g1, g2])
s2 = Squadra("Cremonese", "Ugo", "Stefano", [g3, g4])
c = Campionato([s1, s2])
c.menu()