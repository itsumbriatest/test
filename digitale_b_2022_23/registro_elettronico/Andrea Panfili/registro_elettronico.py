class Classe:
    def __init__(self, grado, sezione, materie, studenti, voti):
        self.grado = grado
        self.sezione = sezione
        self.materie = materie
        self.studenti = studenti
        self.voti = voti
class Registro: 
        def __init__(self, classi):
            self.classi = classi
             
            s1 = Studente ("Andrea", "Panfili")
            s2 = Studente ("Massi", "Muzi")
            self.lista_studenti_classe1 = [andrea, massi]

            italiano = Materia ("Italiano")
            matematica = Materia ("Matematica")
            self.lista_materie_classe1 = [italiano, matematica]

            v1 = Voto (7, s1, italiano, "17/2/2023")
            v2 = Voto (4, s1, matematica, "11/2/2023")
            v3 = Voto (9, s2, italiano, "17/2/2023")
            v4 = Voto (6, s2, matematica, "11/2/2023")
            self.lista_voti_classe1 = [v1, v2, v3, v4]
        
      
        
            s3 = Studente ("Lorenzo", "Scianca")
            s4 = Studente ("Tommaso", "Sabbi")
        #self.lista_studenti_classe2 = [lorenzo, tommaso]
        #
        #storia = Materia ("Storia")
        #scienze = Materia ("Scienze")
        #self.lista_materie_classe2 = [storia, scienze]
        #
        #v5 = Voto (5, lorenzo, italiano, "17/2/2023")
        #v6 = Voto (3, lorenzo, matematica, "11/2/2023")
        #v7 = Voto (8, tommaso, italiano, "17/2/2023")
        #v8 = Voto (10, tommaso, matematica, "11/2/2023")



        def AggiungiVoto(self):
            for i in range(len(self.lista_studenti_classe1)):
                print(i, ")", self.lista_studenti_classe1[i])
            nome_stud = int(input("Di quale studente vuoi inserire il nuovo voto?"))
            stud = self.lista_materie_classe1[nome_stud]

            for i in range(len(self.lista_materie_classe1)):
                print(i, ")", self.lista_materie_classe1[i])
            nome_mat = int(input("Di quale materia vuoi inserire il nuovo voto?"))
            mat = self.lista_materie_classe1[nome_mat]

            data = input("Inserisci la data del voto: ")
            punteggio = float(input("Inserire il punteggio del voto: "))
            voto = Voto(punteggio, stud, mat, data)

            self.lista_voti_classe1.append(voto)


    
          



class Studente:
    #attributo nome e cognome
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
class Materia:
    #attributo nome
    def __init__(self, nome):
        self.nome = nome


class Voto:
    def __init__(self, punteggio, studente, materia, data) -> None:
        self.punteggio = punteggio
        self.studente = studente
        self.materia = materia
        self.data = data
        
        