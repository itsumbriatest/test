from bottle import Bottle, request, response, HTTPResponse

app = Bottle()

# Dati globali
squadre = []
giocatori = []

class Squadra:
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget
        self.rosa = {'portieri': [], 'difensori': [], 'centrocampisti': [], 'attaccanti': []}

class Giocatore:
    def __init__(self, nome, ruolo, costo):
        self.nome = nome
        self.ruolo = ruolo
        self.costo = costo

def cerca_squadra(nome_squadra):
    for squadra in squadre:
        if squadra.nome == nome_squadra:
            return squadra
    return None

def calcola_budget(nome_squadra):
    squadra = cerca_squadra(nome_squadra)
    if squadra is not None:
        budget = squadra.budget
        for giocatore in squadra.rosa['portieri'] + squadra.rosa['difensori'] + squadra.rosa['centrocampisti'] + squadra.rosa['attaccanti']:
            budget -= giocatore.costo
        return budget
    return None

@app.route('/crea_squadra', method='POST')
def crea_squadra():
    data = request.json
    nome_squadra = data['nome']
    budget_totale = int(data['budget'])
    
    if calcola_budget(nome_squadra) is not None:
        return HTTPResponse(status=400, body='Squadra già esistente!')
    
    if budget_totale > 500:
        return HTTPResponse(status=400, body='Il budget totale non può superare 500 fantacrediti!')
    
    squadra = Squadra(nome_squadra, budget_totale)
    squadre.append(squadra)
    
    return 'Squadra creata con successo!'

@app.route('/inserisci_giocatore', method='POST')
def inserisci_giocatore():
    data = request.json
    nome_squadra = data['nome_squadra']
    nome_giocatore = data['nome_giocatore']
    ruolo_giocatore = data['ruolo']
    costo_giocatore = int(data['costo'])
    
    squadra = cerca_squadra(nome_squadra)
    
    if squadra is None:
        return HTTPResponse(status=400, body='Squadra non trovata!')
    
    if calcola_budget(nome_squadra) is None:
        return HTTPResponse(status=400, body='Squadra non trovata!')
    
    if costo_giocatore > calcola_budget(nome_squadra):
        return HTTPResponse(status=400, body='Budget insufficiente per acquistare questo giocatore!')
    
    if ruolo_giocatore == 'portiere' and len(squadra.rosa['portieri']) >= 3:
        return HTTPResponse(status=400, body='Limite di portieri raggiunto!')
    elif ruolo_giocatore == 'difensore' and len(squadra.rosa['difensori']) >= 8:
        return HTTPResponse(status=400, body='Limite di difensori raggiunto!')
    elif ruolo_giocatore == 'centrocampista' and len(squadra.rosa['centrocampisti']) >= 8:
        return HTTPResponse(status=400, body='Limite di centrocampisti raggiunto!')
    elif ruolo_giocatore == 'attaccante' and len(squadra.rosa['attaccanti']) >= 6:
        return HTTPResponse(status=400, body='Limite di attaccanti raggiunto!')
    
    giocatore = Giocatore(nome_giocatore, ruolo_giocatore, costo_giocatore)
    
    if ruolo_giocatore == 'portiere':
        squadra.rosa['portieri'].append(giocatore)
    elif ruolo_giocatore == 'difensore':
        squadra.rosa['difensori'].append(giocatore)
    elif ruolo_giocatore == 'centrocampista':
        squadra.rosa['centrocampisti'].append(giocatore)
    elif ruolo_giocatore == 'attaccante':
        squadra.rosa['attaccanti'].append(giocatore)
    
    return 'Giocatore inserito nella squadra con successo!'

@app.route('/lista_squadre', method='GET')
def lista_squadre():
    nomi_squadre = [squadra.nome for squadra in squadre]
    return {'squadre': nomi_squadre}

@app.route('/leggi_giocatori_squadra', method='POST')
def leggi_giocatori_squadra():
    data = request.json
    nome_squadra = data['nome_squadra']
    
    squadra = cerca_squadra(nome_squadra)
    
    if squadra is None:
        return HTTPResponse(status=400, body='Squadra non trovata!')
    
    rosa_squadra = {
        'portieri': [giocatore.nome for giocatore in squadra.rosa['portieri']],
        'difensori': [giocatore.nome for giocatore in squadra.rosa['difensori']],
        'centrocampisti': [giocatore.nome for giocatore in squadra.rosa['centrocampisti']],
        'attaccanti': [giocatore.nome for giocatore in squadra.rosa['attaccanti']]
    }
    
    return {'rosa_squadra': rosa_squadra}

if __name__ == '__main__':
    app.run(debug=True)
