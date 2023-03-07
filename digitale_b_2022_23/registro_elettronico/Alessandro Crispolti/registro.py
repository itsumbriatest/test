import random

class Classe:
    def __init__(self, grado, sezione):
        stud1 = Studente("Alessandro", "Arancioni")
        stud2 = Studente("Michele", "Rossi")
        stud3 = Studente("Leonardo", "Verdi")
        stud4 = Studente("Lorenzo", "Neri")
        mat1 = Materia("Matematica")
        mat2 = Materia("Italiano")
        mat3 = Materia("Scienze")
        mat4 = Materia("Storia")
        voto1 = Voto(stud1, mat1, "29 Ottobre 2020", random.randint(3,11))
        voto2 = Voto(stud2, mat2, "13 Gennaio 2020", random.randint(3,11))
        voto3 = Voto(stud3, mat3, "23 Novembre 2020", random.randint(3,11))
        voto4 = Voto(stud4, mat4, "1 Aprile 2020", random.randint(3,11))
        self.lista_studenti = [studente1, studente2, studente3, studente4]
        self.lista_materie = [mat1, mat2, mat3, mat4]
        self.lista_voti = [voto1, voto2, voto3, voto4]
        self.grado = grado 
        self.sezione = sezione
        c1 = Classe(1,"A")
        c2 = Classe(2,"A")
        c3 = Classe(3,"A")
        c4 = Classe(4,"A")

    def registro(self):
        scelta = 0
        while scelta != 4:
            print("Registro")
            print("*******************************************")
            print("1) Inserisci un voto")
            print("2) Calcola la media di uno studente")
            print("3) Calcola la media di una classe su una materia")
            print("4) Esci")

            if scelta == "1":
                self.inserisci_voto()
            if scelta == "2":
                self.media_studente()
            if scelta == "3":
                pass

    def inserisci_voto(self):
        self.mostra_studente()
        s = input("Inserisci lo studente: ")
        m = input("Inserisci la materia: ")
        d = input("Inserisci una data: ")
        v = float(input("Inserisci un voto: "))
        voto5 = Voto(s, m, d, v)
        self.lista_voti.append(voto5)

    def media_studente(self):
        self.mostra_studente()
        somma = 0
        i = 0
        for voto in lista_voti:
            somma = somma + self.lista_voti[i]
            i = i + 1
        media = somma / len(self.lista_voti)
        print(media)

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def mostra_studente(self):
        print("Nome: ", self.nome, "Cognome: ", self.cognome)

class Materia:
    def __init__(self, nome_materia):
        self.nome_materia = nome_materia

class Voto:
    def __init__(self, studente, materia, data, voto):
        self.studente = studente
        self.materia = materia 
        self.data = data
        self.voto = voto

#Main
c = Classe()
c.registro()