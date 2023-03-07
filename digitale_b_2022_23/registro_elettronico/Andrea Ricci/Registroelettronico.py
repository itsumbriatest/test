class Classe:
    def __init__(self,listastud,listamat,listavot):
        self.listastud=listastud
        self.listamat=listamat
        self.listavot=listavot

    def menu(self):
        scelta = ""
        while scelta != "4":
            print("1) Aggiungi voto")
            print("2) Media studente")
            print("3) Media materia")
            print("4) Esci")
            scelta = input("Scelta? ")
            

class Materia:
    def __init__(self, nome):
        self.nome=nome

class Studente:
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
class Voto:
    def __init__(self,voto,data,materia,studente):
        self.voto=voto
        self.data=data
        self.materia=materia
        self.studente=studente




# Main
#materia, studente, voto classe

m1=Materia("Matematica")
m2=Materia("Storia")
m3=Materia("Inglese")
m4=Materia("Informatica")

s1=Studente("Andrea","Ricci")
s2=Studente("Riccardo","Troiani")
s3=Studente("Matteo","Ceccarelli")
s4=Studente("Alessio","Silvestrelli")
s5=Studente("Joshua", "Pasahol")
s6=Studente("Rocco","Fonte")
s7=Studente("Alessandro","Crispolti")


v1=Voto(7.5,"3marzo",m1,s1)
v2=Voto(8,"7marzo",m2,s2)
v3=Voto(9,"3maggio",m3,s3)
v4=Voto(10,"9settembre",m4,s4)
v5=Voto(8,"7ottobre",m4,s5)
v6=Voto(4,"13maggio",m1,s6)
v7=Voto(10,"14febbraio",m4,s7)

listas= [s1,s2,s3,s4,s5,s6,s7]
votis=[v1,v2,v3,v4,v5,v6,v7]
listamat=[m1,m2,m3,m4]
classe_3c = Classe(listas, listamat, votis)
classe_3c.menu()