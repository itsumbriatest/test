from datetime import *

def is_lezione(giorno):
    w = giorno.weekday() #0 lunedi.... 6 domenica
    if w == 5 or w == 6:
        return False
    elif giorno >= date(2023, 4, 8) and giorno <= date (2023, 4, 10):
        return False
    elif giorno == date(2023, 4, 25):
        return False
    elif giorno == date(2023, 5, 1):
        return False
    elif giorno == date(2023, 6, 2):
        return False
    else:
        return True
    
oggi = date.today()
fine_lezioni = date(2023, 7, 31)

giorni = 0
while oggi <= fine_lezioni:
    oggi = oggi + timedelta(days=1)
    lezione = is_lezione(oggi)
    if lezione:
        giorni = giorni + 1
    print(oggi, lezione)
print("Giorni = ", giorni)
