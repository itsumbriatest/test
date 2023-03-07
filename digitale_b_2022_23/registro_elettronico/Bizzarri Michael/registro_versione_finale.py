def mostra_lista(oggetti):
    i = 0
    for o in oggetti:
        print(i, o)
        i += 1

class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return self.cognome + " " + self.nome

class Materia:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome

class Voto:
    def __init__(self, studente, materia, punteggio, data):
        self.studente = studente
        self.materia = materia
        self.punteggio = punteggio
        self.data = data

class Classe:
    def __init__(self, grado, sezione, materie, studenti, voti):
        self.grado = grado
        self.sezione = sezione
        self.materie = materie
        self.studenti = studenti
        self.voti = voti
    
    def __str__(self):
        return str(self.grado) + self.sezione
        #return f"{self.grado}{self.sezione}"
    
    def media_studente(self, studente):
        somma = 0
        conta = 0
        for v in self.voti:
            if v.studente == studente:
                somma += v.punteggio
                conta += 1
        return somma / conta
    
    def media_materia(self, materia):
        somma = 0
        conta = 0
        for v in self.voti:
            if v.materia == materia:
                somma += v.punteggio
                conta += 1
        return somma / conta

    def media_classe(self):
        somma=0
        conta=0
        for v in self.voti:
            somma+=v.punteggio
            conta+=1
        return somma/conta



class Registro:
    def __init__(self, classi):
        self.classi = classi
    
    def menu(self):
        scelta = ""
        while scelta != "5":
            print("1) Inserisci voto")
            print("2) Media studente")
            print("3) Media materia")
            print("4) Classe migliore")
            print("5) Esci")
            scelta = input("Scelta: ")
            if scelta == "1":
                self.inserisci_voto()
            elif scelta == "2":
                self.media_studente()
            elif scelta == "3":
                self.media_materia()
            elif scelta == "4":
                self.media_classe_max()
    
    def media_studente(self):
        # Scelgo la classe
        mostra_lista(self.classi)       # <------
        c = int(input("Quale classe? "))
        classe = self.classi[c]
        # Scelgo lo studente
        mostra_lista(classe.studenti)   # <------
        s = int(input("Quale studente?"))
        studente = classe.studenti[s]
        media = classe.media_studente(studente)
        print("Media:", media)
    
    def media_materia(self):
        # Scelgo la classe
        mostra_lista(self.classi)       # <------
        c = int(input("Quale classe? "))
        classe = self.classi[c]
        # Scelgo la materia
        mostra_lista(classe.materie)    # <------
        m = int(input("Quale materia? "))
        materia = classe.materie[m]
        media = classe.media_materia(materia)
        print("Media:", media)
    
    def inserisci_voto(self):
        # Scelgo la classe
        mostra_lista(self.classi)       # <------
        c = int(input("Quale classe? "))
        classe = self.classi[c]
        # Scelgo la materia
        mostra_lista(classe.materie)    # <------
        m = int(input("Quale materia? "))
        materia = classe.materie[m]
        # Scelgo lo studente
        mostra_lista(classe.studenti)   # <------
        s = int(input("Quale studente?"))
        studente = classe.studenti[s]
        # Voto e data
        punteggio = float(input("Quale voto? "))
        data = input("Quale data? ")
        voto = Voto(studente, materia, punteggio, data)
        classe.voti.append(voto)

        def media_classe_max(self):
            maxc=self.classi[0].media_classe()
            maxn=str(self.classi[0])
            #for c in self.classi:
            for i in range(len(self.classi)):
                c = self.classi[i]
                media=c.media_classe()
                if maxc<media:
                    maxc=media
                    maxn=str(c)

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
r.menu()