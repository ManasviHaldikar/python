 #Kite flying program
 
def fly_high():

        print("There are four different kites available right now.\n")
                
        Kite_1={'shape': 'dimond shaped', 'color' : 'blue'}
        Kite_2={'shape': 'rectangular', 'color' : 'green'}
        Kite_3={'shape': 'triangular', 'color': 'purple'}
        Kite_4={'shape': 'triangular', 'color': 'yellow'}
                
        print("I'd like the " + Kite_1 ['color'] + ", "+ Kite_1['shape']+ "kite" )
        print("I'd like the "+ Kite_3 ['color'] + ", "+ Kite_3['shape']+ "kite")
        
        # Create a list of four dictionaries
        kites_availible = [Kite_1, Kite_2, Kite_3, Kite_4]
        kites_availible.remove(Kite_1)
        kites_availible.remove(Kite_2)
        
        
        kites_left= len(kites_availible)
        print(str(kites_left)+ "kites are left that have these features:")
        print(kites_availible)
                
        print("\nLet's fly our kites!")
