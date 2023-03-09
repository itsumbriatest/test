# Tombola "smart"
# ---------------
# Creo una lista di numeri da 1 a 90 (in
# quest'ordine), la mescolo ed infine
# presento i numeri uno per volta
# nell'ordine in cui si trovano nella
# lista mescolata.

import random
numeri = list(range(1, 91))
random.shuffle(numeri)
for n in numeri:
    print("Ho estratto", n)
    input()
