class DispositivoUSB:
    def __init__(self):
        lino = Attore("Lino", "Banfi", 86)
        rocco = Attore("Rocco", "Siffredi", 58)
        natale = Film("Natale a 5 stelle", lino, rocco, 2018, 90)
        zaa = Film("My Name is Zaawaadi", lino, rocco, 2014, 105)
        self.lista_film = [natale, zaa]

    def menu(self):
        scelta = 0
        while scelta != "7":
            print("MENU")
            print("------------------------")
            print("1) Modifica titolo")
            print("2) Modifica durata")
            print("3) Somma tutte le durate")
            print("4) Anagrafica attori")
            print("5) Film più lungo")
            print("6) Film più corto")
            print("7) Esci")
            scelta = input("Scelta? ")
            if scelta == "1":
                self.modifica_titolo()
            elif scelta == "2":
                self.modifica_durata()
            elif scelta == "3":
                self.durata_totale()
            elif scelta == "4":
                self.anagrafica()
            elif scelta == "5":
                self.massimo()
            elif scelta == "6":
                self.minimo()
    
    def mostra_film(self):
        i = 0
        for film in self.lista_film:
            print(i, film.titolo, film.durata)
            i = i + 1
    
    def modifica_titolo(self):
        self.mostra_film()
        f = int(input("Quale film? "))
        nuovo_titolo = input("Quale titolo? ")
        self.lista_film[f].titolo = nuovo_titolo

    def modifica_durata(self):
        self.mostra_film()
        f = int(input("Quale film? "))
        nuova_durata = int(input("Quale durata? "))
        self.lista_film[f].durata = nuova_durata

    def durata_totale(self):
        tot = 0
        for film in self.lista_film:
            tot = tot + film.durata
        print("Durata totale:", tot)

    def anagrafica(self):
        self.mostra_film()
        titolo = input("Titolo del film: ")
        for film in self.lista_film:
            if film.titolo == titolo:
                film.attore1.presentati()
                film.attore2.presentati()

    def massimo(self):
        parziale = self.lista_film[0]
        for film in self.lista_film:
            if film.durata > parziale.durata:
                parziale = film
        print(parziale.titolo, parziale.durata)

    def minimo(self):
        parziale = self.lista_film[0]
        for film in self.lista_film:
            if film.durata < parziale.durata:
                parziale = film
        print(parziale.titolo, parziale.durata)
    
class Film:
    def __init__(self, titolo, attore1, attore2, anno, durata):
        self.titolo = titolo
        self.attore1 = attore1
        self.attore2 = attore2
        self.anno = anno
        self.durata = durata

class Attore:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età
    
    def presentati(self):
        print("Ciao, sono", self.nome, self.cognome, "ed ho", self.anni, "anni")

# Main
d = DispositivoUSB()
d.menu()
