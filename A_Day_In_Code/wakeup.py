#The Day before our epic day
def are_you(feeling):
    if feeling == "excited":
        print("We can't wait for tomorrow")
    
    dragons = 0
    for dragon_count in range (1,5):
        dragons = dragons + dragon_count

    print("I counted "+ str(dragons)+ " dragons and fell asleep") 
    
def time(clock_time):
    time_of_day="AM"
    if clock_time == 9 and time_of_day== "AM":
        alarm="on"
        print("It's 9 AM! The alarm just turned " + alarm)
        print("Wake up and stretch!")
    else: 
        alarm="off"
        print("Go back to sleep, the alarm is "+ alarm)
    


    
    
        
       