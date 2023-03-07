class classe:
    def __init__(self):
        paolo= studente("paolo","noni")
        gino= studente("gino","otto")
        carlo= studente("carlo","grigi")
        fabio= studente("fabio","bianchi")
        self.lista_studente = [paolo, gino, carlo, fabio]
        italiano = materia("italiano")
        matematica= materia("matematica")
        inglese= materia("inglese")
        informatica= materia("informatica")
        self.lista_materie = [italiano,matematica, inglese, informatica]
        v1 = voto(paolo, 7, italiano, "06/03/2023")
        v2= voto(gino, 8, inglese, "10/03/2023")
        v3= voto(fabio, 6, informatica, "11/03/2023")
        self.lista_voti = [v1, v2, v3]

    def menu(self):
        scelta = 0
        while scelta != "5":
            print("menu")
            print("---------------------")
            print("1) inserisci voto")
            print("2) media studente")
            print("3) media classe")
            print("4) media classe più alta")
            print("5) esci")
            scelta = input("scelta? ")
            if scelta =="1":
                self.inserisci_voto()
            elif scelta == "2":
                self.media_studente()
            elif scelta == "3":
                self.media_materia()

    def mostra_materia(self):
        i=0
        for materia in self.lista_materie:
            print(i, materia.mat)
            i=i+1

    def mostra_studente(self):
        i=0
        for sudente in self.lista_studente:
            print(i, studente.cognome, studente.nome)
            i=i+1
    
    def inserisci_voto(self):
        self.mostra_materia()
        m= int(input("quale materia?"))
        self.mostra_studente()
        s = int(input("Quale studente? "))
        p = float(input("Quale voto? "))
        d = input("Quale data? ")
        v = voto(self.lista_studente[s], p, self.lista_materie[m], d)
        self.lista_voti.append(v)
        print(v)

    def media_studente(self):
        self.mostra_studente()
        s = int(input("Quale studente? "))
        somma=0
        cont=0
        for voto in self.lista_voti:
            if voto.studente == self.lista_studente[s]:
                somma =somma + voto.votazione
                cont =cont + 1
        med = somma/ cont
        print(med)

    def media_materia(self):
        self.mostra_materia()
        m = int(input("Quale materia? "))
        somma=0
        cont=0 
        for voto in self.lista_voti:
            if voto.materia == self.lista_materie[m]:
                somma =somma + voto.votazione
                cont =cont + 1
        med = somma/ cont
        print(med)    


class materia:
    def __init__(self, mat):
        self.mat= mat
    
    def __str__(self):
        return self.mat

class studente:
    def __init__(self,nome, cognome):
        self.nome=nome
        self.cognome=cognome
    
    def __str__(self):
        return self.cognome + " " + self.nome

class voto:
    def __init__(self,studente, votazione, materia, data):
        self.studente=studente
        self.votazione=votazione
        self.materia=materia
        self.data=data
    
    def __str__(self):
        return str(self.studente) + " " + str(self.materia) + " " + str(self.votazione) + " " + self.data

# Main
d = classe()
d.menu()