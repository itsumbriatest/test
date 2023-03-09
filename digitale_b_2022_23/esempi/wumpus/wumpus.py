import random
print("Benvenuti nel mondo del Wumpus!")
pos = [1, 1]  # lista di due elementi x, y
treasure = [random.randint(1, 10), random.randint(1, 10)]
monster = [random.randint(1, 10), random.randint(1, 10)]
print("Non devi assolutamente sapere che...")
print("... il tesoro è in", treasure)
print("... e il mostro è in", monster)
# Se treasure e monster coincidono estraggo di nuovo
# monster fino a quando non sono diversi
while treasure == monster:
    monster = [random.randint(1, 10), random.randint(1, 10)]
gameover = False
while gameover == False:
    action = input("Where? (w/a/s/d) ")
    if action == "w":
        pos[1] -= 1
        if pos[1] == 0:
            pos[1] = 10
    elif action == "s":
        pos[1] += 1
        if pos[1] == 11:
            pos[1] = 1
    elif action == "a":
        pos[0] -= 1
        if pos[0] == 0:
            pos[0] = 10
    elif action == "d":
        pos[0] += 1
        if pos[0] == 11:
            pos[0] = 1
    else:
        print("Invalid selection")
    
    print("Nuova posizione:", pos)
    # Dopo lo spostamento verifico se
    # ho vinto o perso

    if pos == treasure:
        print("Hai vinto!")
        gameover = True
    elif pos == monster:
        print("Hai perso...")
        gameover = True