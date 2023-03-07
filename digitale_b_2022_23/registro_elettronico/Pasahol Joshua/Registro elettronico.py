class Classe:
    def __init__(self):
        It = Materia("Italiano")
        Ing = Materia("Inglese")
        Mat = Materia("Matematica")
        bianchi = Studente("Laura", "Bianchi")
        giallo = Studente("Aurora", "Giallo")
        blu = Studente("Anna", "Blu")
        self.lista_studenti =[bianchi, giallo, blu]
        self.lista_materie = [It, Ing, Mat]
        v1 = Voto(bianchi, 9, Ing, "03/06/2023")
        v2 = Voto(blu, 10, Mat, "03/09/2023")
        v3 = Voto(giallo, 3, It, "02/04/2023")
        self.lista_voti = [v1, v2, v3]

    def menu(self):
        scelta = 0
        while scelta != 5:
            print("Menu")
            print("-------------------")
            print("1) Assegna un voto")
            print("2) Calcolare la media di uno studente")
            print("3) Calcolare la media di una classe")
            print("4) La media piu alta")
            print("5) Per uscire")
            scelta = int(input("Scelta? "))
            if scelta == 1:
                self.inserire_voto()
            elif scelta == 2:
                self.media_studente()
            elif scelta == 3:
                self.mostra_materia()
                

    def mostra_materia(self):
        i = 0
        for materia in self.lista_materie:
            print(i, materia.mate)
            i = i + 1

    def mostra_studente(self):
        i = 0
        for Studente in self.lista_studenti:
            (i, Studente.nome, Studente.cognome)
            i = i + 1

    def inserire_voto(self):
        self.mostra_materia()
        m = int(input("Quale materia?"))
        self.mostra_studente()
        s = int(input("Quale studente?"))
        g = float(input("Quale voto?"))
        d = input("Quale data?")
        v = Voto (self.lista_studenti[s], g, self.lista_materie[m], d)
        self.lista_voti.append(v)

    def media_studente(self):
        self.mostra_studente
        s = int(input("Quale studente?"))
        somma = 0
        contatore = 0
        for voto in self.lista_voti:
            if voto.studente == self.lista_studenti[s]:
                somma = somma + voto.voto
                contatore = contatore + 1
            media = somma/contatore
            print(media)

    def media_classe(self):
        self.mostra_materia()
        m = int(input("Quale materia?"))
        somma = 0
        contatore = 0
        for voto in self.lista_voti:
            if voto.materia == self.lista_materie[m]:
                somma = somma + voto.voto
                contatore = contatore + 1
            media = somma/contatore
            print(media)

class Materia:
    def __init__(self, mate):
        self.mate = mate

    def __str__(self):
        return self.mate

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

class Voto:
    def __init__(self, studente, voto, materia, data):
        self.studente = studente
        self.voto = voto
        self.materia = materia
        self.data = data

    def __str(self):
        return str(self.studente) + " " + str(self.materia) + " " + str(self.voto) + " " + self.data
#Main
l = Classe()
l.menu()