
# You don’t always have to start from scratch when writing a class. If the class 
# you’re writing is a specialized version of another class you wrote, you can
# use inheritance.
# When one class inherits from another, it takes on the attributes and methods of the first class.
# The original class is called the parent class, and the new class is the child class. The child class can inherit any
# or all of the attributes and methods of its parent class, but it’s also free to
# define new attributes and methods of its own.

class Car:
#A simple attempt to represent a car.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
   
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
   
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
# battry class for electric car
class Battery:
    #A simple attempt to model a battery for an electric car.
    def __init__(self,battery_size=75):
    #Initialize the battery's attributes.
        self.battery_size = battery_size
    #Initialize the battery's attributes.
    def describe_battery(self):
        print(f'this car has a {self.battery_size}-kwh battery.')
    
    def get_range(self):
        #Print a statement about the range this battery provides.
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")




#create a child class
class ElectricalCar(Car): # car is the parent class
    #Represent aspects of a car, specific to electric vehicles
    def __init__(self,make,model, year):
        #Initialize attributes of the parent class.        
        super().__init__(make,model,year) #super() method lets you access methods from a parent class from within a child class
        # ^Initialize methods of the parent class.
        self.battery_size = 75
        self.battery = Battery()

    def describe_battery(self):
        #Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kWh battery.")



my_tesla = ElectricalCar('Tesela','Model s', 2022)

print(my_tesla.get_descriptive_name())
# 
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
