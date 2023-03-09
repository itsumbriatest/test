# Tombola "ingenua"
# -----------------
# Estraggo un numero controllando
# che non sia già presente nella
# lista di quelli estratti in
# precedenza

import random
estratti = []
for i in range(90):
    print("Estraggo un numero...")
    n = random.randint(1, 90)
    while n in estratti:
        n = random.randint(1, 90)
    estratti.append(n)
    print("Ho estratto", n)
    input()
