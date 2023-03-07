class classe:
    def __init__(self):
        jan = Studente ("jan","tito",self.voto)
        giacomo = Studente("giacomo","popoli",0)
        self.lista_studenti = [jan,giacomo]
        matematica = materie("matematica")
        italiano = materie ("italiano")
        geografia = materie("geografia")
        self.lista_materie = [matematica,italiano,geografia]
    
    def menu(self):
        scelta = 0
        while scelta !="4":   
            print(" SCEGLI LO STUDENTE")
            self.mostra_studenti()
            scelta = input("\nScelta?")
            if(scelta=="0"):
                print("\nSCEGLI LA MATERIA")
                self.mostra_materie()
                scelta1 = input("\nScelta?")
                if(scelta1 =="0"):
                    self.inserisci_voti()
                elif(scelta1 =="1"):
                    self.inserisci_voti()
                elif(scelta1 =="2"):
                    self.inserisci_voti()
            elif(scelta=="1"):
                print("\nSCEGLI LA MATERIA")
                self.mostra_materie()
                scelta1 = input("\nScelta?")
                if(scelta1 =="0"):
                    self.inserisci_voti()
                elif(scelta1 =="1"):
                    self.inserisci_voti()
                elif(scelta1 =="2"):
                    self.inserisci_voti()
            self.mostra_studenti()
    def mostra_materie(self):
        c = 0
        for materia in self.lista_materie :
            print(c,")",materia.nomeM)
            c = c + 1

    def inserisci_voti(self):
        nuovo_voto = int(input("Inserire voto: "))
        self.voto = nuovo_voto

    def mostra_studenti(self):
        i = 0
        for studente in self.lista_studenti:
            print(i,")",studente.cognomeS,studente.nomeS,studente.voto)
            i = i + 1

class materie:
    def __init__(self,nome):
        self.nomeM = nome

class Studente:
    def __init__(self,nome,cognome,voto):
        self.nomeS = nome
        self.cognomeS = cognome
        self.voto = voto
class voto:
    def __init__(self,voto1,data):
        self.voto1 = voto1
        self.data = data

#main 
c = classe()
c.menu()