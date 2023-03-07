class Classe:
    def __init__(self):
        #studenti
        studente = Studente("Giorgia","Meloni")
        studente2 = Studente("Silvio","Berlusconi")
        studente3 = Studente("Matteo","Salvini")
        #materia
        materia = Materia("Economia")
        materia2 = Materia("Diritto")
        materia3 = Materia("Legge")
        #voti
        voti = Voti(studente,materia,"25/05/1990",10)
        voto2 = Voti(studente2,materia2,"09/06/1970",9)
        voto3 = Voti(studente3,materia3,"26/09/1995",8)

        self.lista_classe = [studente,studente2,studente3,voti,voto2,voto3]
        self.lista_materia = [materia,materia2,materia3]



class Studente:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome

class Materia:
    def __init__(self,materia):
        self.nome = materia

class Voti:
    def __init__(self,studente, mateiria,data,voto):
        self.voto = voto
        self.materia = mateiria
        self.data = data
        self.studente = studente



#main
c = Classe()