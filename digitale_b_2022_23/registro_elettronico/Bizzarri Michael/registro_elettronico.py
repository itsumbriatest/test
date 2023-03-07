class Classe:
    m=Materia("Italiano")
    m2=Materia("Matematica")
    m3=Materia("Inglese")
    materie=[m,m2,m3]
    
    s=Studente("Giorgio","Vanni")
    s2=Studente("Marco","Rossi")
    s3=Studente("Mario","Bianchi")
    studenti=[s,s2,s3]

    v=Voto(8,studenti[0],materie[0],"2022-06-27")
    v2=Voto(4,studenti[0],materie[0],"2022-06-25")
    v3=Voto(7,studenti[0],materie[0],"2022-06-13")
    v4=Voto(8,studenti[0],materie[1],"2022-06-17")
    v5=Voto(4,studenti[0],materie[1],"2022-06-04")
    v6=Voto(8,studenti[0],materie[1],"2022-06-30")
    v7=Voto(6,studenti[0],materie[2],"2022-04-09")
    v8=Voto(4,studenti[0],materie[2],"2022-01-13")
    v9=Voto(4,studenti[0],materie[2],"2022-01-17")

    v10=Voto(5,studenti[1],materie[0],"2022-01-13")
    v11=Voto(8,studenti[1],materie[0],"2022-01-13")
    v12=Voto(2,studenti[1],materie[0],"2022-01-10")
    v13=Voto(1,studenti[1],materie[1],"2022-01-03")
    v14=Voto(4,studenti[1],materie[1],"2022-01-07")
    v15=Voto(9,studenti[1],materie[1],"2022-01-05")
    v16=Voto(1,studenti[1],materie[2],"2022-01-06")
    v17=Voto(5,studenti[1],materie[2],"2022-01-09")
    v18=Voto(7,studenti[1],materie[2],"2022-01-04")

    v19=Voto(2,studenti[2],materie[0],"2022-01-22")
    v20=Voto(9,studenti[2],materie[0],"2022-01-23")
    v21=Voto(4,studenti[2],materie[0],"2022-01-25")
    v22=Voto(8,studenti[2],materie[1],"2022-01-23")
    v23=Voto(7,studenti[2],materie[1],"2022-01-13")
    v24=Voto(6,studenti[2],materie[1],"2022-01-15")
    v25=Voto(0,studenti[2],materie[2],"2022-01-27")
    v26=Voto(4,studenti[2],materie[2],"2022-01-19")
    v27=Voto(3,studenti[2],materie[2],"2022-01-26")

    voti=[v,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27]


    def menu(self):
        scelta=0
        while scelta!="5":
            print("MENU")
            print("------------------------")
            print("(1) Inserisci un voto")
            print("(2) Media studente di una classe")
            print("(3) Media di una materia di una classe")
            print("(4) Classe con media più alta")
            print("(5) EXIT")
            scelta=input("Scelta? ")

    def aggiungi(self):
        for voti in self.voti:
            if 

class Studente:
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome

class Voto:
    def __init__(self,voto,studente,materia,data):
        self.voto=voto
        self.studente = studente
        self.materia = materia
        self.data = data

class Materia:
    def __init__(self,nome):
        self.nome=nome

#Main
d=Classe()

#ciao