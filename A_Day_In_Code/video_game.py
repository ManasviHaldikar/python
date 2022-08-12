# VIDEO game and cookies program


def snack_n_game(bake_timer, videogame):
    # Enter a numerical value (for example, 10 instead of "ten")
    waiting = True
    while waiting:
        if bake_timer==0:
            waiting= False
        else:
            print("Timer: " + str(bake_timer)) 
            bake_timer-=1    #this means bake_timer= Bake_timer-1
        
    print("\nLet's Play "+ videogame.title()+ " now!")       
        