from datetime import *
print("I miei prossimi 10 compleanni")
WEEKDAYS = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
for i in range(10):   # RICORDA: i va da 0 a 9
	birthday = date(2024 + i, 1, 16)
	w = birthday.weekday()  # RICORDA: weekday va da 0 a 6
	print(WEEKDAYS[w])	