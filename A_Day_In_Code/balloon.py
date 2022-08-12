#Balloon Darts Program
def pop():
 Balloons_popped= 5
 if Balloons_popped>0 and Balloons_popped<=2:
            dragon_size= "small"
 elif Balloons_popped>= 3 and Balloons_popped<5:
            dragon_size= "medium"
 elif Balloons_popped==5:
            dragon_size= "large"
 else:
            dragon_size=""
            print("Try again!")
 if dragon_size:
            print("You won a " + dragon_size+" dragon!")
            

from tkinter.tix import Balloon
from turtle import color


def choose_balloons(*our_choice):
    balloons=[] #create empty list
    for color_choice in our_choice:
        balloons.append(color_choice + ' balloon')
        print("I got a " + color_choice+ ' balloon')
    return balloons # return list

def travel(transport, destination= 'our house'):
    print("\n We are " + transport + " to "+ destination + ".")
    
balloon_colors= ['yellow', 'blue', 'purple', 'green', 'red', 'pink']
del balloon_colors[4]# delete 'red'
for balloon in balloon_colors:
    print("Availible balloon color: " + balloon.title ()) 

def pick():
    first_balloons= choose_balloons ('blue', 'purple') #functional call
    second_balloons= first_balloons[:]
    for balloon in second_balloons:
        print("I got another "+ balloon)
        
    del balloon_colors [1:3] # delete 'blue' and 'purple'
    print("Balloon colors still availible: " +  str(balloon_colors))

    travel('walking') # function call
            
                