class Classe:
    def __init__(self, sezione, listaStudenti, listaMateria, listaVoti):
        self.listaStudenti = listaStudenti
        self.listaMateria = listaMateria
        self.listaVoti = listaVoti
        self.sezione = sezione

    def inserireVoto(self):
        i = 0
        voto = input("Inserisci voto: ")
        for materia in self.listaMateria:
            print(i, materia.nomeMat)
            i = i + 1
        materia = input("Inserisci numero materia: ")
        i = 0
        for studente in self.listaStudenti:
            print(i, studente.nome)
            i = i + 1
        studente = input("Inserisci numero studente: ")
        v = Voto(int(voto), self.listaMateria[int(materia)], " data ", self.listaStudenti[int(studente)])
        self.listaVoti.append(v)

    def media_singolo_studente(self): 
        i = 0
        for studente in self.listaStudenti:
            print(i, studente.nome)
            i = i + 1
        studente = input("Inserisci numero studente: ")
        somma = 0
        contatore = 0
        for voto in self.listaVoti:
            if voto.studente == self.listaStudenti[int(studente)]:
                somma = somma + voto.punteggio
                contatore = contatore + 1
        media = somma/contatore
        print("La media è: ", media)

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
class Materie:
    def __init__(self, nomeMat):
        self.nomeMat = nomeMat

class Voto:
    def __init__(self, punteggio, materia, dataVoto, studente):
        self.punteggio = punteggio
        self.materia = materia
        self.datavoto = dataVoto
        self.studente = studente

#MAIN      

m1 = Materie("Matematica")
m2 = Materie("Chimica")
m3 = Materie("Italiano")
m4 = Materie("Inglese")

s1 = Studente("Kiara", "Guerrero")
s2 = Studente("Rocco", "Fonte")
s3 = Studente("Matti", "Ceccarelli")
s4 = Studente("Adriana", "Freire")

v1 = Voto(7, m1, "14/11/2022", s1)
v2 = Voto(10, m2, "15/07/2022", s2)
v3 = Voto(3, m3, "20/08/2022", s3)
v4 = Voto(8, m4, "14/11/2022", s4)
v5 = Voto(6, m1, "14/07/2022", s3)
v6 = Voto(5, m1, "20/08/2022", s2)
v7 = Voto(9, m2, "18/11/2022", s4) 
v8 = Voto(6, m3, "14/07/2022", s1)
v9 = Voto(4, m4, "18/08/2022", s2) 
v10 = Voto(8, m1, "14/08/2022", s1)
v11 = Voto(9, m2, "14/11/2022", s2)
v12 = Voto(10, m3, "14/08/2022", s3)
v13 = Voto(9, m4, "14/11/2022", s4)
v14 = Voto(7, m2, "14/08/2022", s1)

c1 = Classe("A",[s1, s2, s3, s4],[m1, m2, m3, m4], [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14])

c1.inserireVoto()
c1.media_singolo_studente()


