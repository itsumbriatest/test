import random
parole = ["qui", "quo", "qua"]
x = random.choice(parole)
storico = []
errori = 0
gameover = False
while gameover == False:
    tentativo = input("Lettera? ")
    storico.append(tentativo)
    if tentativo not in x:
        errori += 1
        print("Attento, hai fatto", errori, "errori")
    if errori == 7:
        print("Hai perso...")
        gameover = True
    else:
        gameover = True
        for lettera in x:
            if lettera in storico:
                print(lettera)
            else:
                gameover = False
                print("*")
        if gameover == True:
            print("Hai vinto!!!")
