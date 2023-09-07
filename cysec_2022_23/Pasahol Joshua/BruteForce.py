#IMPLEMENTA UN ATTACCO BRUTE -FORCE
#CONTRO IL CIFRARIO DI CESARE

from Code import decifra_cesare 

if __name__ == "__main__":
    cipher_text = "CRUUR"
    print("Proviamo tutte le chiavi con", cipher_text)
    for text in  range(26):
        print(decifra_cesare(cipher_text, text))


