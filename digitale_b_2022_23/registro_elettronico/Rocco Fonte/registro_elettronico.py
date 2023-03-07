class Classe:
    def __init__(self, sezione, lista_materie, lista_studenti, lista_voti):
        self.sezione = sezione
        self.lista_materie = lista_materie
        self.lista_studenti = lista_studenti
        self.lista_voti = lista_voti
    def inserisci_voto(self):
        i = 0
        voto = input("Inserisci un voto: ")
        for materia in self.lista_materie:
            print(i, materia.nome)
            i = i + 1
        materia = input("Inserisci numero materia: ")
        i = 0
        for studente in self.lista_studenti:
            print(i, studente.nome, studente.cognome)
            i = i + 1
        studente = input("Inserisci numero studente: ")
        v = Voto(int(voto), self.lista_materie[int(materia)], "data", self.lista_studenti[int(studente)])
        self.lista_voti.append(v)
    def media_singolo_studente(self):
        i = 0
        for studente in self.lista_studenti:
            print(i, studente.nome, studente.cognome)
            i = i + 1
        studente = input("Inserisci numero studente: ")
        somma = 0
        contatore = 0
        for voto in self.lista_voti:
            if voto.studente == self.lista_studenti[int(studente)]:
                somma = somma + voto.punteggio
                contatore = contatore + 1
        media = somma/contatore
        print("La media è", media)
    def media_materia(self):
        i = 0
        for materia in self.lista_materie:
            print(i, materia.nome)
            i = i + 1
        materia = input("Inserisci numero materia: ")
        somma = 0
        contatore = 0
        for voto in self.lista_voti:
            if voto.materia == self.lista_materie[int(materia)]:
                somma = somma + voto.punteggio
                contatore = contatore + 1
        media = somma/contatore
        print("La media è", media)

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
class Voto:
    def __init__(self, punteggio, materia, data, studente):
        self.punteggio = punteggio
        self.materia = materia
        self.data = data
        self.studente = studente
class Materia:
    def __init__(self, nome):
        self.nome = nome



#main
m1 = Materia("Storia")
m2 = Materia("Matematica")
m3 = Materia("Inglese")

s1 = Studente("A","AA")
s2 = Studente("B","BB")
s3 = Studente("C","CC")

v1 = Voto(7, m1, "07-02-2021", s1)
v2 = Voto(2, m1, "07-02-2021", s2)
v3 = Voto(7, m2, "07-02-2021", s3)
v4 = Voto(8, m3, "07-02-2021", s2)
v5 = Voto(5, m2, "07-02-2021", s2)

c1 = Classe("A",[m1,m2,m3],[s1,s2,s3],[v1,v2,v3,v4,v5])

c1.inserisci_voto()
c1.media_singolo_studente()
c1.media_materia()
#lista_classi = [c1]