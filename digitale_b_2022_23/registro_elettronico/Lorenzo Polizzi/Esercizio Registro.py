class Classe:
    def __init__(self):
        storia = Materie("storia")
        geografia = Materie ("geografia")
        arte = Materie("arte")
        matematica = Materie("matematica")

        rocco = Studente("Rocco", "Siffredi")
        lino = Studente("Lino", "Banfi")
        gianni = Studente("Gianni", "Cani")
        carlo = Studente("Carlo", "Conti")

        
        self.lista_materie = [storia, geografia, arte, matematica]
        self.lista_studenti = [rocco, lino, gianni, carlo]

        voto1 = Voti(self.lista_materie[0], self.lista_studenti[0], "10/08/2022", 9)
        voto2 = Voti(self.lista_materie[1], self.lista_studenti[1], "20/07/2021", 4)
        voto3 = Voti(self.lista_materie[2], self.lista_studenti[2], "15/04/2023", 6)
        voto4 = Voti(self.lista_materie[3], self.lista_studenti[3], "12/12/2020", 8)
        self.lista_voti = [voto1, voto2, voto3, voto4]

    def menu(self):
        scelta = 0
        while (scelta != 7):
            print("MENU")
            print("------------------------------")
            print("1) Inserisci voto")
            scelta = int(input("Scelta? "))
            if scelta == 1:
                self.inserisci_voto()

    
    def inserisci_voto(self):
        materia_scelta = int(input("Inserisci la materia da 0 a 3: "))
        studente_scelto = int(input("Inserisci lo studente da 0 a 3: "))
        voto_nuovo = int(input("Inserisci un nuovo voto: "))
        voto5 = Voti(self.lista_materie[materia_scelta], self.lista_studenti[studente_scelto], "06/03/2023", voto_nuovo)
        self.lista_voti.append(voto5)
        print(voto5)


class Materie:
    def __init__(self, nome):
        self.nome = nome

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.voti = []

class Voti:
    def __init__(self, materia, studente, data, voto):
        self.materia = materia
        self.studente = studente
        self.data = data
        self.voto = voto

Classe().menu()