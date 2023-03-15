from datetime import *

oggi = datetime.now()
fine_lezioni = datetime(2023, 7, 31)

giorni = 0
while oggi <= fine_lezioni:
    oggi = oggi + timedelta(days = 1)
    giorni = giorni + 1
    print(oggi)
print("giorni =", giorni)