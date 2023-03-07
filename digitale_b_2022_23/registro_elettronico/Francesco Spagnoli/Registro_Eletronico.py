class Classe:
    def __init__(self):
        #studenti
        st1 = Studente("Piper","Carta")
        st2 = Studente("Piero","Torno in dietro")
        st3 = Studente("Alexander","Kalashikov")
        st4 = Studente("Pino","Abete")
        self.lista_studente = [st1,st2,st3,st4]

        #materie
        m1 = Materia("C++")
        m2 = Materia("JAVA")
        self.lista_materia = [m1,m2]

        #voti
        v1 = Voto(st1, m1, "2023-03-06", 6.5)
        v2 = Voto(st1, m1, "2022-12-05", 4)
        v3 = Voto(st2, m2, "2023-01-16", 7)
        self.lista_voti = [v1,v2,v3]

    def Menu(self):
        scelta=0
        while scelta != '7':
            print("MENU")
            print('================================================================')
            print("1) Aggiungi un voto")
            print("2) Calcolare la media di uno studente")
            print("3) Calcolare la media della classe")
            scelta = input("Scelta")
            if scelta == '1':
                self.Aggiungi_Voto()
            elif scelta == '2':
                self.Calcola_media_Studente

    def Aggiungi_Voto(self):
        for i in  range(len(self.lista_studente)):
            print(i, ")", self.lista_studente[i].cognome)
        ns = int(input("Di quale studente vuoi aggiungere un voto? "))
        stud = self.lista_studente[ns]

        for i in range(len(self.lista_materia)):
            print(i, ")", self.lista_materia[i].nomeM)
        nm = int(input("Di quale materia vuoi aggiundere il voto? "))
        mater = self.lista_materia[nm]

        data = input("Data del voto? ")
        punteggio = float(input("Quale punteggio? "))
        voto = Voto(stud, mater, data, punteggio)
        self.lista_voti.append(voto)

    def Calcola_media_Studente(self):
        for i in  range(len(self.lista_studente)):
            print(i, ")", self.lista_studente[i].cognome)
        ns = int(input("Di quale studente vuoi aggiungere un voto? "))
        stud = self.lista_studente[ns]

        for i in range(len(self.lista_voti)):
            tot = tot + self.lista_voti[i]
        media = tot/len(self.lista_voti)
        print("La media di ", self.lista_studente[ns], " è", media)

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

class Materia:
    def __init__(self,nomeM):
        self.nomeM = nomeM

class Voto:
    def __init__(self, studente, materia, data, voto):
        self.studente = studente
        self.materia = materia
        self.data = data
        self.voto = voto

#Main
test = Classe()
test.Menu()