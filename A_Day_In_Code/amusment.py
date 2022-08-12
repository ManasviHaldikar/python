# Amusment park program
def fun_ride():
 ticket_cost, tickets=15,2
 print("The total cost is $"+  str(ticket_cost* tickets))
        
 attractions=["carousel","bouncy castle", "slide", "roller castle", "ferris wheel"] 
 closed_attraction= attractions.pop(3)    
 print("\nThe "+ closed_attraction + " is closed today \n")
        
 print("The open attractions are: ")
 for attraction in attractions:
            print(attraction.title())
        
 if "bouncy castle" in attractions :
            print("\n Let's go to the bouncy castle!") 
            
 castle_full= False
 if not castle_full:
            print("\n We're jumping in the bouncy castle!")