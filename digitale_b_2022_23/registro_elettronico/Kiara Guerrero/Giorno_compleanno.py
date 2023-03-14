from datetime import *

print("Giorni dei miei prossimi compleanni")
WEEKDAYS = ["Lunedí", "Martedí", "Mercoledí", "Giovedí", "Venerdí", "Sabato", "Domenica"]
for i in range(10):
    birtaday = date(2024 + i, 11, 25)
    w = birtaday.weekday()
    print(WEEKDAYS[w])
