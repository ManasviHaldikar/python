#Build a salad program
# Class definition
class Salad():
    """Modeling a salad"""
    
    def __init__(self,dressing, size):
        """" Initialize attributes that describe the salad """
        self.dressing= dressing   # assign dressing value to dressing attribute
        self.size = size   # assign size value to size attribute
        
    def salad_mix(self, *ingredients):
        """Add ingredients to the salad."""
        for ingredient in ingredients:
            print (ingredient + " added to the "+ self.dressing + " salad.")
            
    def choose_bowl(self):
        """Choose appropriate bowl for the salad size."""
        print(self.size + " bowl for the "+ self.dressing + " salad.\n")

def yum_yum(dressing, size):
# Create objects (Instances) from Salad Class
    salad_one = Salad(dressing, size)
    #Call methods on Salad class objects
    salad_one.choose_bowl()
    salad_one.salad_mix('lettuce', 'cheese', 'carrots', 'celery', 'tomatoes')
        