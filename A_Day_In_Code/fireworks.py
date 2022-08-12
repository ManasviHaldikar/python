# Fireworks show program

#Function definition
from token import SOFT_KEYWORD


def watch_fireworks():
    minutes=0
    while True:
        minutes+=1
        if minutes< 15:
            continue            # go back to the beginning of the loop
        
        minutes_left= 20- minutes
        if minutes<19:
           print("Amazing grand finale! Minutes left:"+ str(minutes_left))
        elif minutes== 19:
            print("One minute left!")
        elif minutes==20:
            print("\n That was a great Fireworks show!\n")
            break    #exit the loop
    
def lit_up_the_sky(sky):
    if sky!="raining":
        watch_fireworks()
    print("let's go home now!")