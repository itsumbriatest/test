# IMPLEMENTA UN ATTACCO BRUTE-FORCE
# CONTRO IL CIFRARIO DI CESARE

import cesare

def brute_force_attack(ciphertext):
    print("Brute Force Attack:")
    for key in range(26):
        decrypted_text = cesare.decifra_cesare(ciphertext, key)
        print(f"Key {key}: {decrypted_text}")

if __name__ == "__main__":
    cipher_text = "CRUUR"
    print("Proviamo tutte le chiavi con", cipher_text)
    brute_force_attack(cipher_text)
