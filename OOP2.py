class Car:
    #A simple attempt to represent a car.

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0

    def get_descriptive(self):
        #Return a neatly formatted descriptive name.
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        #Print a statement showing the car's mileage
        print(f"This car has {self.odometer_reding} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reding:
            self.odometer_reding = mileage
        else:
            print("you can't roll back an odometer")

    print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles <= 0:
            print("you can't add negative miles")
        else:
            self.odometer_reding += miles
    #Add the given amount to the odometer reading.



my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


my_used_car.increment_odometer(-100)


