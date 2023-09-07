# Implementa un attacco brute-force contro il cifrario di Cesare

import cesare

if __name__ == "__main__":
    cipher_text = "CRUUR"
    print("Proviamo tutte le chiavi con", cipher_text)
    for key in range(1, 27):
        print(cesare.decifra_cesare(cipher_text, key))