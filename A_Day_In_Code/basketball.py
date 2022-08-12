# Basketball program
import random
throw_result=('through hoop','miss')
 
# function definitions
def shoot_hoops(player_number):
    player_score = 0
    for throw in range(15):
         player_result= random.choice(throw_result)
         if player_result=='through hoop':
            player_score+=1 # this means player_score=player_score= player_score+ 1
            print(player_number+ "score :"+ str(player_score))
            return player_score
        
def commpare_scores(player_1_score, player_2_score):
    if player_1_score >player_2_score:
        print("/n Player #1 got a higher score!") 
    elif player_2_score> player_1_score:
        print("/nPlayer #2 got a higher score!")
    else:
        print("/n It's a tie")
               
def play():
    player_1_score= shoot_hoops('Player #1')
    player_2_score= shoot_hoops('Player #2')
    commpare_scores(player_1_score, player_2_score)