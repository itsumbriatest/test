def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1


class Squadra:
    def _init_(self, nome, allenatore, presidente, calciatore1, calciatore2):
        self.nome = nome
        self.allenatore = allenatore
        self.presidente = presidente
        self.calciatore1 = calciatore1
        self.calciatore2 = calciatore2
    
    def _str_(self):
        return self.nome + " " + self.allenatore + " " + self.presidente + " " + self.calciatore1 + " " + self.calciatore2

    def cambiaNome(self, nome):
        self.nome = nome

class Campionato:
    def _init_(self, squadra, partita):
        self.squadra = squadra
        self.partita = partita

class Calciatore:
    def _init_(self, nome, anno, forza):
        self.nome = nome 
        self.anno = anno 
        self.forza = forza
    
    def _str_(self):
        return self.nome + " " + str(self.anno) + " " + str(self.forza)

    def cambiaAnagrafica(self, nome, anno):
        self.nome = nome
        self.anno = anno

    def cambiaForza (self, forza):
        if self.forza >= 100 and self.forza <= 0:
            self.forza = forza


#main

Roma = Squadra("Roma", "Giorgio", "Magella", "Silvio", "Luca")
Terni = Squadra("Frosinone", "San Basilio", "Marotti", "Gigi", "Ugo")
print(Roma)
g1 = Calciatore("Marco", 1997, 60)
g1.cambiaAnagrafica("Luca", 1700)
print(g1)
g1.cambiaForza(90)
print(g1)