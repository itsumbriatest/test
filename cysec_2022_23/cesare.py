# Esempio di crittografia simmetrica
# con il celeberrimo cifrario di Cesare

def cifra_cesare(clear_text, key):
    cipher_text = ""
    num_letters = ord("Z") - ord("A") + 1
    for letter in clear_text:
        if "A" <= letter <= "Z":
            cipher_text += chr((ord(letter) - ord("A") + key) % num_letters + ord("A"))
        elif "a" <= letter <= "z":
            cipher_text += chr((ord(letter) - ord("a") + key) % num_letters + ord("a"))
        else:
            cipher_text += letter
    return cipher_text

def decifra_cesare(cipher_text, key):
    return cifra_cesare(cipher_text, -key)

if __name__ == "__main__":
    print("CIFRATURA DI CESARE")
    clear_text = input("TESTO IN CHIARO: ")
    key = int(input("CHIAVE: "))
    cipher_text = cifra_cesare(clear_text, key)
    print("TESTO CIFRATO:", cipher_text)
