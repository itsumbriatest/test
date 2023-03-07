class Classe:
    def __init__(self):
        italiano = Materia("Italiano")
        storia = Materia("Storia")
        matematica = Materia("Matematica")
        inglese = Materia("Inglese")
        motoria = Materia("Motoria")
        geografia = Materia("Geografia")
        rocco = Studente("Rocco", "Siffredi")
        lino = Studente("Lino", "Banfi")
        self.lista_studenti = [rocco, lino]
        self.lista_materia = [italiano, storia]

    def mostra_materia(self):
        i = 0
        for materia in self.lista_materia:
            print(i, materia.nome)
            i = i + 1

    def mostra_studente(self):
        i = 0
        for studente in self.lista_studenti:
            print(i, studente.nome, studente.cognome)
            i = i + 1

    def inserisci_voto(self):
        self.mostra_materia()
        mat = input("Materia: ")
        for materia in self.lista_materia:
            if materia.nome == mat:
                self.mostra_studente()
                stud = input("Studente: ")
                for studente in self.lista_studenti:
                    if studente.nome


class Materia:
    def __init__(self, nome):
        self.nome = nome

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

class Voto:
    def __init__(self, materia, studente, data):
        self.materia = materia
        self.studnete = studente
        self.data = data