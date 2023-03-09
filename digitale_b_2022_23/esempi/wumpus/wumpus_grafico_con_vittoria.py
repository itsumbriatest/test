# Programma PyGame di base

# Importa ed inizializza la libreria PyGame
import pygame
from pygame.locals import *

pygame.init()

# Imposta la finestra dove andremo a disegnare
screen = pygame.display.set_mode((500, 500))


# Definiamo alcuni colori che andremo a usare in seguito
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Funzioni di supporto per disegnare gli FPS
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
def update_fps():
    fps = f"{int(clock.get_fps())} FPS"
    fps_text = font.render(fps, 1, RED)
    return fps_text

# Questo è il "game loop", ovvero un ciclo dove
# viene gestito l'evolversi del gioco che termina
# quando l'utente invia il comando di chiusura
# (es. premendo la "X" per chiudere la finestra)
running = True  # Running vuol dire "in esecuzione"
x = 1
y = 1
x_mostro, y_mostro = 3, 4
x_tesoro, y_tesoro = 10, 3
mostro = False
tesoro = False
n = 1
while running == True:
    
    ##########################################################
    # Prima parte del game loop: gestione degli eventi
    ##########################################################

    # L'utente ha cliccato sulla "X" per chiudere la finestra?
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_q:
                running = False
            elif mostro == False and tesoro == False:
                if event.key == K_w and y > 1:
                    y = y - 1
                elif event.key == K_s and y < 10:
                    y = y + 1
                elif event.key == K_a and x > 1:
                    x = x - 1
                elif event.key == K_d and x < 10:
                    x = x + 1
        
        if x == x_mostro and y == y_mostro:
            mostro = True
        
        if x == x_tesoro and y == y_tesoro:
            tesoro = True

    ##########################################################
    # Seconda parte del game loop: disegno del fotogramma
    ##########################################################

    # Riempiamo (fill) lo sfondo di bianco
    if mostro == True:
        screen.fill(RED)
    elif tesoro == True:
        screen.fill(GREEN)
    else:
        screen.fill(WHITE)

    # Scriviamo gli FPS sullo schermo
    screen.blit(update_fps(), (10, 0))

    # Disegniamo la griglia
    for i in range(11):
        pygame.draw.line(screen, LIGHT_GREY, (0, i * 50), (500, i * 50))
        pygame.draw.line(screen, LIGHT_GREY, (i * 50, 0), (i * 50, 500))
        pygame.draw.line(screen, GREEN, (0, i * 50), (i * 50, 500))
        pygame.draw.line(screen, GREEN, (0, 500 - i * 50), (500 - i * 50, 500))
    

    # Disegniamo la posizione del giocatore
    pygame.draw.circle(screen, BLUE, (x * 50 - 25, y * 50 - 25), 10)

    # Sorpresa! Fino ad ora i disegni che abbiam fatto erano
    # soltanto in memoria, per maggior velocità; questo comando,
    # il flip, letteralmente "ribalta" il contenuto del disegno
    # in memoria sullo schermo, rendendolo così visibile
    clock.tick(60)
    pygame.display.flip()

# Tutto fatto (siamo fuori dal while, quindi running non è
# più uguale a True), chiudiamo PyGame!
pygame.quit()