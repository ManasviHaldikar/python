 #Beach Program
def build_castle(building_sandcastle, pretzel_bag, donut_box):
  flags= ('red','blue')
  print("We have " + flags[0] + " & " + flags[1]+ " flags for the sandcastle.")

  if pretzel_bag== "open" or donut_box== "open": # outer if statement
         if building_sandcastle:# inner if statement
             print("\n Seagulls are eating")
         else:
             print("\n Watching out for seagulls")
  else:
            print("\n Seagulls are not eating")
             
             