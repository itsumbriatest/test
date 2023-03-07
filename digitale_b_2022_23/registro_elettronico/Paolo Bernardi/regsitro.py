class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

class Materia:
    def __init__(self, nome):
        self.nome = nome

class Voto:
    def __init__(self, studente, materia, punteggio, data):
        self.studente = studente
        self.materia = materia
        self.punteggio = punteggio
        self.data = data

class Classe:
    def __init__(self, grado, sezione, materie, studenti, voti):
        self. grado = grado
        self.sezione = sezione
        self.materie = materie
        self.studenti = studenti
        self.voti = voti

class Registro:
    def __init__(self, classi):
        self.classi = classi

# Main
m1 = Materia("Italiano")
m2 = Materia("Matematica")
s1 = Studente("Paolo", "Bernardi")
s2 = Studente("Piero", "Brandola")
s3 = Studente("Antonio", "Gramsci")
s4 = Studente("Napoleone", "Bonaparte")
v1 = Voto(s1, m1, 7, "2023-03-06")
v2 = Voto(s2, m2, 5.5, "2023-03-07")
v3 = Voto(s3, m1, 6, "2023-03-01")
v4 = Voto(s4, m1, 4, "2023-01-16")
c1 = Classe(1, "A", [m1, m2], [s1, s2], [v1, v2])
c2 = Classe(2, "B", [m1, m2], [s3, s4], [v3, v4])
r = Registro([c1, c2])