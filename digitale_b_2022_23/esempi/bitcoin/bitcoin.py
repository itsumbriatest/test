with open("bitcoin.csv") as f:
    linee = f.readlines()

print("Ho caricato", len(linee), "linee")

prezzi = []
for l in linee[1:]:
    v = l.split(",")
    prezzo_chiusura = int(float(v[4]))
    prezzi.append(prezzo_chiusura)

print(prezzi)