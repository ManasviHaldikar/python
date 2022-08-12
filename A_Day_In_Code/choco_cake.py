#Cake for dessert program
class Dessert():
    """Modeling a dessert."""
    
    def __init__(self, size, cost):
        self.size = size
        self.cost = cost

    def about_dessert(self):
        print("\nThis "+ self.size+ " dessert is "+ self.cost + ".")

class Cake(Dessert):
    """Modeling a desert which is a cake"""
       
    def __init__(self, size, cost):
        super().__init__(size, cost)
        self.cake_type = "Vanilla"
    
    def order_toppings(self, toppings):
        print("we would like these toppings on the cake: ")
        for topping in toppings:
            print(topping.title())

def bake():      
    our_cake= Cake('large', '$20')
    our_cake.cake_type = "Chocolate"
    print("We're ordering a "+ our_cake.cake_type+ " cake.\n")

    cake_toppings= ('chocolate frosting', 'vanilla cream \n')
    our_cake.order_toppings(cake_toppings)
    our_cake.about_dessert()
