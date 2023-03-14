from datetime import *

def sab_dom(giorno):
    sd = giorno.weekday()
    if sd == 5 or sd == 6:
        return True
    else:
        return False
    
WEEKDAYS = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
def compleanno(giorno):
    for i in range(10):
        comple = date(2024 + i, 2, 26)
        c = comple.weekday()
        print(WEEKDAYS[c])

oggi = date.today()
fine_mondo = date(2012, 12, 21)

giorni = 0
while oggi >= fine_mondo:
    fine_mondo = fine_mondo + timedelta(days = 1)
    if sab_dom(fine_mondo):
        giorni += 1
    print(fine_mondo)
print("Giorni =", giorni)

print("I miei prossimi 10 compleanni: ")
compleanno(oggi)