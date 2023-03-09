# Programma PyGame di base
# ------------------------
# I.I.S. Casagrande-Cesi
# Sistemi Informativi Aziendali

# Importa ed inizializza la libreria PyGame
import pygame
from pygame.locals import *

pygame.init()

# Imposta la finestra dove andremo a disegnare
screen = pygame.display.set_mode((500, 500))

# Definiamo alcuni colori che andremo a usare in seguito
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Questo è il "game loop", ovvero un ciclo dove
# viene gestito l'evolversi del gioco che termina
# quando l'utente invia il comando di chiusura
# (es. premendo la "X" per chiudere la finestra)
running = True  # Running vuol dire "in esecuzione"
while running == True:

    ##########################################################
    # Prima parte del game loop: gestione degli eventi
    ##########################################################

    for event in pygame.event.get():
        # L'utente ha cliccato sulla "X" per chiudere la finestra?
        if event.type == pygame.QUIT:
            running = False
        # L'utente ha premuto il tasto "q" (ovvero "Quit", uscire)?
        elif event.type == KEYDOWN:
            if event.key == K_q:
                running = False

    ##########################################################
    # Seconda parte del game loop: disegno del fotogramma
    ##########################################################

    # Riempiamo (fill) lo sfondo di bianco
    screen.fill(WHITE)

    # Tanto per fare un esempio, disegnamo un cerchio blu
    # in mezzo alla finestra
    pygame.draw.circle(screen, BLUE, (250, 250), 75)
    
    # Sempre come prova, disegnamo una bella linea nera diagonale
    pygame.draw.line(screen, BLACK, (0, 0), (500, 500))

    # Sorpresa! Fino ad ora i disegni che abbiam fatto erano
    # soltanto in memoria, per maggior velocità; questo comando,
    # il flip, letteralmente "ribalta" il contenuto del disegno
    # in memoria sullo schermo, rendendolo così visibile
    pygame.display.flip()

# Tutto fatto (siamo fuori dal while, quindi running non è
# più uguale a True), chiudiamo PyGame!
pygame.quit()