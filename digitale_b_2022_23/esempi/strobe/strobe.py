# PyGame strobe
# -------------
#
# Rispetto ai programmi fatti fino ad ora questo va a tutto schermo
# e fa i calcoli delle coordinate da disegnare in modo da adattarsi
# alla risoluzione attuale (finora invece avevamo usato risoluzioni
# fisse, come 500x500 pixels).

import os
from random import randint
import sys

# Importa ed inizializza la libreria PyGame
import pygame
from pygame.locals import *


pygame.init()
info = pygame.display.Info() 
screen_width, screen_height = info.current_w, info.current_h

pygame.mixer.init()

# Finestra a schermo intero, woohoo!!!!!
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Definiamo alcuni colori che andremo a usare in seguito
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Funzioni di supporto per regolare gli FPS
clock = pygame.time.Clock()

# Questo è il "game loop", ovvero un ciclo dove
# viene gestito l'evolversi del gioco che termina
# quando l'utente invia il comando di chiusura
# (es. premendo la "X" per chiudere la finestra)
running = True  # Running vuol dire "in esecuzione"

# Se True disegno lo sfondo bianco, altrimenti nero
alternato = True

pygame.mixer.music.load("bass.mp3")
pygame.mixer.music.play(-1)  # -1 significa loop infinito

bc = pygame.image.load("bitcoin.png")
bc_width = bc.get_width()
bc_height = bc.get_height()

while running == True:
    # 1. Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_q:
                running = False
    
    # 2. Gestione della logica
    alternato = not alternato   # Se alternato è True così diventa False
                                # altrimenti avviene il contrario
    # 3. Disegno
    if alternato == True:
        screen.fill(WHITE)
    else:
        screen.fill(BLACK)
    
    x = screen_width - bc_width
    y = screen_height - bc_height
    screen.blit(bc, (randint(0, x), randint(0, y)))

    clock.tick(60) # Regolazione degli FPS
                   # Più questo numero è alto, più rapidamente si alterna lo strobe
                   # e più rapidamente si muove il simbolo del BitCoin

    pygame.display.flip()

# Tutto fatto (siamo fuori dal while, quindi running non è
# più uguale a True), chiudiamo PyGame!
pygame.quit()
