
# Pizza ordering Program

def pizza_type(size, crust):
       print("I would like a ")
   
#Function definition
def calculate_cost(Total_pizzas, total_toppings, pizza_cost):
    total_cost= Total_pizzas* pizza_cost + total_toppings * topping_cost
    return total_cost
            
# These variables have a float data type since the numbers have a decimal point
small_cost, medium_cost, large_cost, topping_cost= 4.99, 7.99, 9.99, 0.99   

toppings=("basil","extra cheese", "pepperoni", "garlic", "peppers", "tomatoes")     
print("We'd like the"+ toppings[1]+ "and"+ "toppings" [3]+ "toppings.")   

def make():
    #Function calls
    pizza_type('medium', 'thick')
    pizza_type(crust= 'crispy thin', size='medium')
    total_pizza_cost= calculate_cost(2,4, medium_cost)

    print("\n The total cost is $" + str(total_pizza_cost)+ ".Enjoy!")
    
def eat():
    table_occupancy={'Chair #1':'empty', 'Chair #2' : 'empty', 'Chair #3': 'empty', 
    'Chair #4': 'empty',}

    #Loop through the dictionary's key:value pairs
    for chair, status in table_occupancy.items():
        print (chair + "is" + status)
        
        print("\nThis table is empty, let's eat here!\n")
        
        #Loop through the dictionary's keys only
        for chair in table_occupancy.keys():
            table_occupancy[chair]='taken'
            print(chair + "is now"+ table_occupancy [chair])
            
        print("\nThe pizza is delicious!")
