from datetime import *

def c_maya(giorno):
    w= giorno.weekday()  #0 lunedì..... 6 domenica
    if w == 5 or w == 6:
        return True
    else:
        return False
    
oggi = date.today()
fine_mondo = date(2012, 12, 21)

giorni=0
while fine_mondo <= oggi:
    fine_mondo = fine_mondo + timedelta(days=1)
    if c_maya(fine_mondo):
        giorni = giorni + 1
print("giorni=", giorni)

print("i prossimi 10 compleanni saranno di")
weekdays = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]

for i in range(10):
    birtheday = date(2024 + i, 3, 27)
    g= birtheday.weekday()
    print(weekdays[g])