class Voto:
    def __init__(self, voto, materia, data, nome):
        self.voto = voto 
        self.materia = materia
        self.data = data
        self.nome = nome


class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome 
        self.cognome = cognome
        self.voti = []

    def addVoto(self, voto):
        self.voti.append(voto)



class Materia:
    def __init__(self, nome):
        self.nome = nome 
        self.voto = []      

    def addVoto(self, voto):
        self.voti.append(voto)

class Classe:
    def __init__(self, nome):
        self.nome = nome
        self.materie = []
        self.studenti = []
        
    def aggiungi_voto(self, studente, materia, voto):
        voto = Voto(voto, materia)
        studente.addVoto(voto)
        materia.add.Voto(voto)



    

