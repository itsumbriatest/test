class Classe:
    def __init__(self, listaMaterie, listaStudenti, listaVoti):
        self.listaM = listaMaterie
        self.listaS = listaStudenti
        self.listaV = listaVoti

    def menu(self):
        scelta = "0"
        while scelta != "4":
            print("MENU'")
            print("=====================")
            print("1 - Aggiungi Voto")
            print("2 - Media Studente")
            print("3 - Media Materie")
            print("4 - Esci")

            scelta = input("Seleziona ")

            #if scelta == "1":
            #    self.modifica_titolo()
            #elif scelta == "2":
            #    self.modifica_durata()
            #elif scelta == "3":
            #    self.durata_totale()

class Studente:
    def __init__(self, nomeStudente, cognomeStudente):
        self.nomeS = nomeStudente
        self.cognomeS = cognomeStudente
    
    def schedaStudente(self):
        print("Alunno ", self.nomeS, self.cognomeS)

class Materia:
    def __init__(self, nomeMateria):
        self.nomeM = nomeMateria

class Voto:
    def __init__(self, votoMateria, dataMateria, Materia_ , Studente_):
        self.Voto = votoMateria
        self.Data = dataMateria
        self.Materia = Materia_
        self.Studente = Studente_

#Main
m1 = Materia("Matematica")
m2 = Materia("Storia")
m3 = Materia("Italiano")
m4 = Materia("Inglese")
m5 = Materia("Motoria")
m6 = Materia("Musica")

s1 = Studente("Pippo", "Baudo")
s2 = Studente("Sandra", "Milo")
s3 = Studente("Genny", "La Carogna")
s4 = Studente("Luca", "Laurenti")
s5 = Studente("Giucas", "Casella")
s6 = Studente("Rosario", "Fiorello")

v1 = Voto(6.5, "15 marzo", m1, s1)
v2 = Voto(4, "30 settembre", m2, s2)
v3 = Voto(9, "21 maggio", m3, s3)
v4 = Voto(7.75, "8 aprile", m4, s4)
v5 = Voto(8, "19 febbraio", m5, s5)
v6 = Voto(5, "3 dicembre", m6, s6)

listaS = [s1, s2, s3, s4, s5, s6]
listaM = [m1, m2, m3, m4, m5, m6]
listaV = [v1, v2, v3, v4, v5, v6]

classe_2b = Classe(listaS, listaM, listaV)
classe_2b.menu()