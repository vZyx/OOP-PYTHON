# 9-1
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")
# create instance
restaurant = Restaurant('the mean queen', 'pizza')
#print the instance's attributes
print(restaurant.name)
print(restaurant.cuisine_type)
# call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 
#Create three different instances from the class, and call describe_restaurant() for each instance.

ludvigs = Restaurant("ludvig's bistro", 'seafood')
mango_thai = Restaurant('mango thai', 'thai food')
mean_queen = Restaurant('the mean queen', 'pizza')

mean_queen.describe_restaurant()
mango_thai.describe_restaurant()
ludvigs.describe_restaurant()






