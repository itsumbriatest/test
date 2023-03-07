class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = {}

    def aggiungi_voto(self, materia, voto):
        self.voti[materia] = voto

    def media_voti(self):
        if len(self.voti) == 0:
            return 0
        return sum(self.voti.values()) / len(self.voti)

class Classe:
    def __init__(self, nome):
        self.nome = nome
        self.materie = []
        self.studenti = {}

    def aggiungi_materia(self, nome_materia):
        self.materie.append(nome_materia)

    def aggiungi_studente(self, nome_studente):
        self.studenti[nome_studente] = Studente(nome_studente)

    def aggiungi_voto(self, nome_studente, nome_materia, voto):
        studente = self.studenti[nome_studente]
        studente.aggiungi_voto(nome_materia, voto)

    def media_voti_studente(self, nome_studente):
        studente = self.studenti[nome_studente]
        return studente.media_voti()

    def media_voti_materia(self, nome_materia):
        voti_materia = []
        for studente in self.studenti.values():
            if nome_materia in studente.voti:
                voti_materia.append(studente.voti[nome_materia])
        if len(voti_materia) == 0:
            return 0
        return sum(voti_materia) / len(voti_materia)

    def media_voti_classe(self):
        media_per_studente = []
        for studente in self.studenti.values():
            media_per_studente.append(studente.media_voti())
        if len(media_per_studente) == 0:
            return 0
        return sum(media_per_studente) / len(media_per_studente)

    def classe_con_media_voti_piu_alta(self, elenco_classi):
        media_voti_per_classe = {}
        for classe in elenco_classi:
            media_voti_per_classe[classe.nome] = classe.media_voti_classe()
        classe_con_media_piu_alta = max(media_voti_per_classe, key=media_voti_per_classe.get)
        return classe_con_media_piu_alta

